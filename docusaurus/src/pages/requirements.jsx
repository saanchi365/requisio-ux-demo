// Requirements: the board's columns, with search and filters (another custom piece).
import React, {useState} from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import data from '@site/src/data/requisio.json';
import {Pill, featureUrl} from '@site/src/components/Bits';

const STATUSES = ['Done', 'In progress', 'To do'];

export default function Requirements() {
  const [feature, setFeature] = useState('All');
  const [status, setStatus] = useState('All');
  const [search, setSearch] = useState('');

  const rows = data.features.flatMap((f) => [
    {...f.board, n: f.n, title: f.name, f, top: true},
    ...f.issues.map((i) => ({...i, f, top: false})),
  ]);
  const shown = rows.filter(
    (r) =>
      (feature === 'All' || r.f.slug === feature) &&
      (status === 'All' || r.status === status) &&
      `#${r.n} ${r.title} ${r.comments}`.toLowerCase().includes(search.toLowerCase()),
  );

  return (
    <Layout title="Requirements" description="Every requirement from the project board">
      <main className="container container--wide margin-vert--lg">
        <h1>Requirements</h1>
        <p className="lead">
          Every requirement from the <a href={data.board}>project board</a>, with the same columns. Use the filters to
          narrow the list.
        </p>

        <div className="filters">
          <input
            type="search"
            placeholder="Search issues and comments"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
          <select value={feature} onChange={(e) => setFeature(e.target.value)} aria-label="Feature">
            <option value="All">All features</option>
            {data.features.map((f) => (
              <option key={f.slug} value={f.slug}>
                {f.name}
              </option>
            ))}
          </select>
          <div className="chips" role="group" aria-label="Status">
            {['All', ...STATUSES].map((s) => (
              <button key={s} type="button" className={status === s ? 'is-active' : ''} onClick={() => setStatus(s)}>
                {s}
              </button>
            ))}
          </div>
          <span className="small">
            {shown.length} of {rows.length} shown
          </span>
        </div>

        <div className="req-table">
          <table>
            <thead>
              <tr>
                {['#', 'Requirement', 'Feature', 'Status', 'Priority', 'Assignee', 'Start date', 'Target date',
                  'Flowchart', 'Wireframe', 'Comments / inputs'].map((h) => (
                  <th key={h}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {shown.map((r) => (
                <tr key={r.n} className={r.top ? 'is-feature' : ''}>
                  <td>
                    <a href={`${data.gh}${r.n}`}>#{r.n}</a>
                  </td>
                  <td>{r.top ? <Link to={featureUrl(r.f.slug)}>{r.title}</Link> : `↳ ${r.title}`}</td>
                  <td>{r.feature}</td>
                  <td>
                    <Pill status={r.status} />
                  </td>
                  <td>{r.priority}</td>
                  <td>{r.assignees.length ? r.assignees.map((a) => `@${a}`).join(', ') : <span className="small">Unassigned</span>}</td>
                  <td>{r.start}</td>
                  <td>{r.target}</td>
                  <td>
                    <Link to={featureUrl(r.f.slug)}>View</Link>
                  </td>
                  <td>
                    <span className="small">None yet</span>
                  </td>
                  <td>{r.comments || <span className="small">—</span>}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </Layout>
  );
}
