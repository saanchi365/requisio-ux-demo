// Issues as a split view: the list on the left, the chosen issue's details on the right.
import React, {useState} from 'react';
import {Pill} from './Bits';
import IssueDetails from './IssueDetails';

export default function IssueExplorer({issues}) {
  const [selected, setSelected] = useState(issues[0].n);
  return (
    <div className="issue-explorer">
      <ul className="issue-explorer__list">
        {issues.map((i) => (
          <li key={i.n}>
            <button
              type="button"
              className={i.n === selected ? 'is-active' : ''}
              onClick={() => setSelected(i.n)}>
              <span className="small">#{i.n}</span>
              <span className="issue-explorer__title">{i.title}</span>
              <Pill status={i.status} />
            </button>
          </li>
        ))}
      </ul>
      <IssueDetails issue={issues.find((i) => i.n === selected)} />
    </div>
  );
}
