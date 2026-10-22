// A flowchart where clicking a box that mentions an issue (#6, #7 …) opens that issue beside the chart.
// This is the kind of "custom interactive piece" MkDocs Material can't do on its own.
import React, {useEffect, useRef, useState} from 'react';
import Mermaid from '@theme/Mermaid';
import flows from '@site/src/data/flows.json';
import IssueDetails from './IssueDetails';

const issueIn = (node) => {
  const match = node.textContent.match(/#(\d+)/);
  return match ? Number(match[1]) : null;
};

export default function ClickableFlowchart({file, issues}) {
  const box = useRef(null);
  const [selected, setSelected] = useState(null);
  const known = new Set(issues.map((i) => i.n));

  // Mermaid draws the chart a moment after the page loads, so mark the clickable boxes whenever it appears.
  useEffect(() => {
    const decorate = () =>
      box.current?.querySelectorAll('g.node').forEach((node) => {
        const n = issueIn(node);
        node.classList.toggle('is-clickable', known.has(n));
        node.classList.toggle('is-selected', n !== null && n === selected);
      });
    decorate();
    const watcher = new MutationObserver(decorate);
    watcher.observe(box.current, {childList: true, subtree: true});
    return () => watcher.disconnect();
  }, [selected]);

  const onClick = (event) => {
    const node = event.target.closest('g.node');
    const n = node && issueIn(node);
    if (known.has(n)) setSelected(n);
  };

  const issue = issues.find((i) => i.n === selected);
  return (
    <div className="flow-explorer">
      <div className="flow-explorer__chart" ref={box} onClick={onClick}>
        <Mermaid value={flows[file]} />
      </div>
      <div className="flow-explorer__details">
        {issue ? (
          <IssueDetails issue={issue} />
        ) : (
          <p className="flow-explorer__hint">Click a box with a #number to see its issue here.</p>
        )}
      </div>
    </div>
  );
}
