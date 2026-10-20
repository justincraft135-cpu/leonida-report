/* Tracker lists. Edit this file to add items after launch.
 * Each item: { id: "unique-id", name: "Shown name", note: "Optional hint", area: "Optional region" }
 * Never reuse or change an id once it's live, because visitors' saved progress uses it.
 */
var TRACKERS = [
  {
    id: "locations",
    title: "Locations",
    intro: "Regions of Leonida shown by Rockstar before launch.",
    items: [
      { id: "vice-city", name: "Vice City", note: "The neon-lit city at the heart of Leonida." },
      { id: "leonida-keys", name: "Leonida Keys", note: "A chain of islands and beaches." },
      { id: "grassrivers", name: "Grassrivers", note: "Wetlands and swamp, home to plenty of wildlife." },
      { id: "port-gellhorn", name: "Port Gellhorn", note: "A run-down port town." },
      { id: "ambrosia", name: "Ambrosia", note: "Farmland and industry inland." },
      { id: "mount-kalaga", name: "Mount Kalaga National Park", note: "Forests, trails and backcountry." }
    ]
  },
  { id: "missions", title: "Missions", intro: "Story and side missions.", items: [] },
  { id: "vehicles", title: "Vehicles", intro: "Cars, bikes, boats and aircraft.", items: [] },
  { id: "collectibles", title: "Collectibles", intro: "Hidden items around Leonida.", items: [] }
];
