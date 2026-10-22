// Small shared pieces: status label, progress bar, side panel, feature cards.
import React from 'react';
import Link from '@docusaurus/Link';
import data from '@site/src/data/requisio.json';

const PILL = {Done: 'done', 'In progress': 'progress', 'To do': 'todo'};

export function Pill({status}) {
  return <span className={`pill pill--${PILL[status] || 'todo'}`}>{status}</span>;
}

export const featureUrl = (slug) => `/docs/features/${slug}/`;

export function SidePanel({children}) {
  return <aside className="side-panel">{children}</aside>;
}

export function PanelSection({title, children}) {
  return (
    <section>
      <h4>{title}</h4>
      {children}
    </section>
  );
}

export function CommentButton({href, children = 'Comment on GitHub'}) {
  return (
    <a className="button button--primary button--block side-panel__button" href={href}>
      {children}
    </a>
  );
}

export function issuesDone(feature) {
  return feature.issues.filter((i) => i.status === 'Done').length;
}

export function ProgressCard({feature}) {
  const done = issuesDone(feature);
  const total = feature.issues.length;
  return (
    <Link className="card-link" to={featureUrl(feature.slug)}>
      <strong className="card-link__title">{feature.name}</strong>
      <span className="card-link__meta">
        {feature.who} · <Pill status={feature.status} />
      </span>
      <span className={`bar bar--${PILL[feature.status]}`}>
        <span style={{width: `${Math.max(Math.round((done / total) * 100), 4)}%`}} />
      </span>
      <span className="small">
        {done} of {total} issues done
      </span>
    </Link>
  );
}

export function FeatureCards() {
  const areas = [...new Set(data.features.map((f) => f.area))];
  return areas.map((area) => (
    <section key={area}>
      <h2>{area}</h2>
      <div className="card-grid">
        {data.features
          .filter((f) => f.area === area)
          .map((f) => (
            <Link key={f.slug} className="card-link" to={featureUrl(f.slug)}>
              <strong className="card-link__title">{f.name}</strong>
              <span className="card-link__text" dangerouslySetInnerHTML={{__html: f.summary}} />
              <span className="card-link__meta">
                {f.who} · <Pill status={f.status} />
              </span>
            </Link>
          ))}
      </div>
    </section>
  ));
}
