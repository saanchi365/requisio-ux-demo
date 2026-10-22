// The left-hand menus: one for Features (grouped by area), one for Users.

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  features: [
    'features/index',
    {type: 'category', label: 'Setting up', collapsible: false, items: ['features/setup-rules']},
    {
      type: 'category',
      label: 'Requesting',
      collapsible: false,
      items: ['features/create-request', 'features/track-requests'],
    },
    {type: 'category', label: 'Approving', collapsible: false, items: ['features/approvals']},
  ],
  users: ['users/user-understanding', 'users/journey-map', 'users/use-cases'],
};

module.exports = sidebars;
