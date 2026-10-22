// Home: numbers row and progress cards in the middle, side panel on the right.
import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import data from '@site/src/data/requisio.json';
import {CommentButton, PanelSection, ProgressCard, SidePanel, featureUrl} from '@site/src/components/Bits';

export default function Home() {
  const issues = data.features.flatMap((f) => f.issues);
  const count = (s) => issues.filter((i) => i.status === s).length;
  const stats = [
    [data.features.length, 'Features', ''],
    [issues.length, 'Issues', ''],
    [count('Done'), 'Done', 'done'],
    [count('In progress'), 'In progress', 'progress'],
    [count('To do'), 'To do', 'todo'],
  ];

  return (
    <Layout title="Home" description="How Requisio works: features, flowcharts, issues and use cases">
      <main className="container container--wide margin-vert--lg">
        <div className="feature-layout">
          <div className="feature-main">
            <h1>Requisio handbook</h1>
            <p className="lead">
              How Requisio works: each feature with its flowchart, issues and use cases, in one place.{' '}
              <em>Requisio is a made-up purchase-request app, used to practise UX documentation.</em>
            </p>

            <div className="stats">
              {stats.map(([num, label, kind]) => (
                <div key={label} className={`stat ${kind ? `stat--${kind}` : ''}`}>
                  <span className="num">{num}</span>
                  <span className="label">{label}</span>
                </div>
              ))}
            </div>

            <h2>Where things stand</h2>
            <div className="card-grid card-grid--2">
              {data.features.map((f) => (
                <ProgressCard key={f.slug} feature={f} />
              ))}
            </div>

            <h2>Find your way</h2>
            <div className="card-grid">
              <Link className="card-link" to="/docs/features/">
                <strong className="card-link__title">Features</strong>
                <span className="card-link__text">One page per feature: an overview, then the flowchart, issues and use cases.</span>
              </Link>
              <Link className="card-link" to="/docs/users/user-understanding/">
                <strong className="card-link__title">Users</strong>
                <span className="card-link__text">Who uses Requisio, their journey, and all use cases.</span>
              </Link>
              <Link className="card-link" to="/requirements/">
                <strong className="card-link__title">Requirements</strong>
                <span className="card-link__text">Every issue from the project board, with filters.</span>
              </Link>
            </div>
          </div>

          <SidePanel>
            <PanelSection title="Needs your input">
              <ul>
                {data.features.flatMap((f) =>
                  f.questions.map((q) => (
                    <li key={q}>
                      {q} <Link to={featureUrl(f.slug)}>{f.name}</Link>
                    </li>
                  )),
                )}
              </ul>
            </PanelSection>
            <PanelSection title="Recently changed">
              <ul>
                <li>{data.updated} · Docusaurus version added</li>
                <li>{data.updated} · Requirements page has all board columns</li>
                <li>{data.updated} · New layout and theme</li>
              </ul>
            </PanelSection>
            <PanelSection title="Last updated">
              <p>{data.updated}</p>
            </PanelSection>
            <CommentButton href="https://github.com/saanchi365/requisio-ux-demo/issues">Give feedback on GitHub</CommentButton>
          </SidePanel>
        </div>
      </main>
    </Layout>
  );
}
