# Homebox UI Editing Instructions for AI Agent

These instructions are extracted from a screencast walkthrough of the Homebox inventory system fork. The AI agent should implement these changes to improve the user interface.

---

## 1. Specs Editability

**Task:** Make the specs field editable on the Overview page.

Currently, specs cannot be edited in the frontend on the overview page. The specs section should allow inline editing.

---

## 2. Add Variant Field to Database

**Task:** Add a new database field called `variant`.

- Field type: `VARCHAR(255)` (short text)
- Purpose: Store product variants (e.g., "120 by 60 cm") separately from the model number
- The model number field should be reserved for the exact manufacturer model number

---

## 3. Fix AI Spec Generation Bug

**Task:** Debug and fix the "Failed to Save specs" error.

The AI spec generation feature (calling Gemini API with product name and variant) is failing to save. This needs debugging and fixing.

---

## 4. AI Spec Generation Logic Update

**Task:** Change the AI spec override behavior.

Current logic: AI is prevented from overriding human-written specs.

New logic: If a human-written spec exists, the AI should append its generated spec after a blank line, allowing the user to manually merge them.

---

## 5. Photo Gallery Pill Labels

**Task:** Add pill/tag labels to photos in the gallery view.

Photos should display a small pill icon indicating their type (e.g., "dimensions", "product", "warranty document"). This allows quick identification.

---

## 6. Reorganize Upload UI

**Task:** Move upload controls beneath the photos card.

Current state: Upload controls (Browse, Camera, Drag and Drop) are in a separate location.

New layout:
- Photos card displays the gallery
- Beneath the photos card, add an upload card with buttons for:
  - Browse (file system)
  - Camera (webcam capture)
  - Drag and drop zone
- Mobile breakpoint: Show Browse and Camera buttons
- Desktop breakpoint: Show Drag and Drop and file system upload options

---

## 7. Media Card Consistency

**Task:** Apply the same UI pattern to the Media card.

- Add pill displays for media types
- Add the same four-part upload card beneath media items
- Maintain responsive breakpoints for mobile vs desktop controls

---

## 8. Future Enhancement: Markdown Editor for Specs

**Task (Lower Priority):** Implement a markdown editor for specs that renders directly into readable format.

Note: This is marked as a "down the line" fix.

---

## 9. Add Item Type Selector to Top Bar

**Task:** Add the ability to change/update item type from the item view.

Current state: Item type can only be set when creating a new item; cannot be updated afterward.

Solution:
- Add "Update Type" button to the top action bar (after "Update Location" and "Put in Box")
- If no type is assigned, show "Generic" and allow type selection
- Types are mutually exclusive (single selection only)

---

## 10. Reorganize Top Bar Actions

**Task:** Simplify the top action bar.

New top bar layout:
- Update Location
- Put in Box
- Update Type

Nest under "Other Actions" dropdown:
- Generate Specs (remove from main bar)
- Suggest Storage
- Giveaway Posts

---

## 11. Notes Tab: Add Delete Confirmation

**Task:** Add a confirmation modal when deleting notes.

Current state: No safety check before deletion.

Required: Display confirmation modal asking "Are you sure you want to delete?" with appropriate toast notification.

---

## 12. Notes Tab: Add Edit Functionality

**Task:** Add the ability to edit existing notes.

Add a small edit icon next to each note that opens an editor and allows updating the note content.

---

## 13. Related Items: Enhanced Selection Dropdown

**Task:** Improve the related items search/selection dropdown.

Current state: Just shows item names (e.g., "torch, torch, torch for car") with no way to distinguish between items.

New dropdown display should show a card for each result containing:
- Item thumbnail
- Item name
- Manufacturer
- Asset ID
- Storage location

---

## 14. Related Items: Enhanced Display Card

**Task:** Improve how related items are displayed once added.

The related item display card should show:
- Thumbnail
- Name
- Asset ID
- Storage location/box

---

## 15. Related Items: Improve User-Facing Messages

**Task:** Make relationship messages more user-friendly.

Replace technical messages with user-friendly alternatives:
- "Remove relation to torch" -> "Remove association" or similar
- "Created relationship" -> "Linked to [item name]" or similar

---

## 16. Purchase and Warranty Tab: Show Associated Media

**Task:** Display purchase/warranty documents in their respective sections.

- Under Purchase section: Show attached invoice/receipt if exists
- Under Warranty section: Show attached warranty document if exists
- In Edit view: Add ability to attach/associate these documents

---

## 17. Purchase and Warranty Tab: Edit View

**Task:** Make purchase information editable.

Current state: Purchase info is visible in View mode but not editable in Edit mode.

Fix: Add purchase info fields to the Edit view.

---

## 18. Future Enhancement: Currency Selection

**Task (Lower Priority):** Add currency selector for purchase price field.

---

## 19. Tab Reordering

**Task:** Change the tab order.

New tab order (left to right):
1. Overview
2. Specs
3. Media
4. Purchase (rename from "Purchase and Warranty")
5. Related
6. Notes (moved to far right)

---

## Summary of Changes

| Priority | Task | Type |
|----------|------|------|
| High | Fix AI spec generation bug | Bug Fix |
| High | Make specs editable on Overview | Feature |
| High | Add variant database field | Database |
| High | Add Update Type to top bar | Feature |
| High | Add note edit functionality | Feature |
| High | Add delete confirmation for notes | UX |
| Medium | Reorganize upload UI | UI Refactor |
| Medium | Enhanced related items dropdown | UX |
| Medium | Tab reordering | UI |
| Medium | User-friendly relationship messages | UX |
| Medium | Purchase/warranty media display | Feature |
| Medium | Purchase info in edit view | Bug Fix |
| Low | Markdown editor for specs | Enhancement |
| Low | Currency selector | Enhancement |
