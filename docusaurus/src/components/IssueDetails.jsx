// Everything about one issue: what was asked, when it's done, and the board's columns.
import React from 'react';
import data from '@site/src/data/requisio.json';
import {Pill} from './Bits';

export default function IssueDetails({issue}) {
  return (
    <div className="issue-details">
      <div className="issue-details__head">
        <span className="small">Issue #{issue.n}</span>
        <Pill status={issue.status} />
      </div>
      <h3>{issue.title}</h3>
      <p>{issue.req}</p>
      <h4>Done when</h4>
      <ul>
        {issue.done.map((d) => (
          <li key={d}>{d}</li>
        ))}
      </ul>
      <dl className="issue-details__facts">
        <div>
          <dt>Assignee</dt>
          <dd>{issue.assignees.length ? issue.assignees.map((a) => `@${a}`).join(', ') : 'Unassigned'}</dd>
        </div>
        <div>
          <dt>Start date</dt>
          <dd>{issue.start}</dd>
        </div>
        <div>
          <dt>Target date</dt>
          <dd>{issue.target}</dd>
        </div>
        <div>
          <dt>Priority</dt>
          <dd>{issue.priority}</dd>
        </div>
      </dl>
      {issue.comments && (
        <>
          <h4>Comments / inputs</h4>
          <p>{issue.comments}</p>
        </>
      )}
      <a href={`${data.gh}${issue.n}`}>Open #{issue.n} on GitHub ↗</a>
    </div>
  );
}
