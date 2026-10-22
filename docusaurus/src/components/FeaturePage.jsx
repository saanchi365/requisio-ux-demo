// One feature page: overview card on top, then tabs, with the side panel beside them.
import React from 'react';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import data from '@site/src/data/requisio.json';
import {CommentButton, PanelSection, Pill, SidePanel} from './Bits';
import ClickableFlowchart from './ClickableFlowchart';
import IssueExplorer from './IssueExplorer';

const ICON = {Done: '✓', 'In progress': '◔', 'To do': '○'};

export default function FeaturePage({slug}) {
  const f = data.features.find((x) => x.slug === slug);
  const issueUrl = (n) => `${data.gh}${n}`;

  // Wireframes come first when a feature has any; otherwise the flowchart opens first.
  const tabs = [];
  if (f.wireframes.length) {
    tabs.push(
      <TabItem key="wireframes" value="wireframes" label="Wireframes">
        {f.wireframes.map((w) => (
          <img key={w.file} src={w.file} alt={w.title} />
        ))}
      </TabItem>,
    );
  }
  tabs.push(
    <TabItem key="flowchart" value="flowchart" label="Flowchart">
      {f.flows.map((flow) => (
        <div key={flow.file}>
          {f.flows.length > 1 && <h3>{flow.title}</h3>}
          <ClickableFlowchart file={flow.file} issues={f.issues} />
        </div>
      ))}
    </TabItem>,
    <TabItem key="issues" value="issues" label="Issues">
      <IssueExplorer issues={f.issues} />
    </TabItem>,
    <TabItem key="usecases" value="usecases" label="Use cases">
      <ol>
        {f.usecases.map((u) => (
          <li key={u} dangerouslySetInnerHTML={{__html: u}} />
        ))}
      </ol>
    </TabItem>,
  );

  return (
    <>
      <div className="overview">
        <p dangerouslySetInnerHTML={{__html: f.summary}} />
        <div className="facts">
          <div>
            <span className="label">Who uses it</span>
            {f.who}
          </div>
          <div>
            <span className="label">Status</span>
            <Pill status={f.status} />
          </div>
          <div>
            <span className="label">Priority</span>
            {f.priority}
          </div>
          <div>
            <span className="label">Target date</span>
            {f.target}
          </div>
          <div>
            <span className="label">Feature issue</span>
            <a href={issueUrl(f.n)}>#{f.n}</a>
          </div>
        </div>
      </div>

      <div className="feature-layout">
        <div className="feature-main">
          <Tabs>{tabs}</Tabs>
        </div>
        <SidePanel>
          <PanelSection title="Issues">
            <ul>
              {f.issues.map((i) => (
                <li key={i.n}>
                  <span className={`st st--${i.status.replace(' ', '-').toLowerCase()}`}>{ICON[i.status]}</span>{' '}
                  <a href={issueUrl(i.n)}>
                    #{i.n} {i.title}
                  </a>
                </li>
              ))}
            </ul>
          </PanelSection>
          <PanelSection title="Open questions">
            <ul>
              {f.questions.map((q) => (
                <li key={q}>{q}</li>
              ))}
            </ul>
          </PanelSection>
          <PanelSection title="Not confirmed yet">
            <ul>
              {f.unconfirmed.map((q) => (
                <li key={q}>{q}</li>
              ))}
            </ul>
          </PanelSection>
          <PanelSection title="Last updated">
            <p>{data.updated}</p>
          </PanelSection>
          <CommentButton href={issueUrl(f.n)} />
        </SidePanel>
      </div>
    </>
  );
}
