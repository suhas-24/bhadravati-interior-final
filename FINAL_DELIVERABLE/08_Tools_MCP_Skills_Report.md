# Tools, MCP & Skills Report — Bhadravati Interior Visualization

**Scope:** Precision interior design + 2D/3D visualization delivery without blocking on install-heavy pipelines.  
**Date:** 2026-08-11

---

## Recommended immediate stack (use for final delivery)

| Layer | Tool | Status | Role |
| --- | --- | --- | --- |
| Design logic | `interior-design-advisor` skill | **Available now** | Zoning, clearances, palette, lighting, specs, prompts |
| Dimensioned layouts | SVG / HTML via `visualise` skill | **Available now** | Floor plans, furniture footprints, circulation diagrams |
| Concept renders | Cursor `GenerateImage` | **Available now** | Mood/room concept stills (label as conceptual) |
| Product research | `cursor-ide-browser` MCP | **Available now** | Local catalogs, prices, finishes, vendor pages |
| Interactive QA | `playwright` / browser MCP | **Available now** | Capture product pages, compare options |
| Structured handoff | Markdown + PDF in `FINAL_DELIVERABLE/` | **Available now** | Client package (plans, specs, visuals) |

**Do not wait on:** Blender MCP, Homestyler/Planner5D APIs, Figma MCP, or Three.js apps for this delivery cycle.

---

## What sibling agents should use right now

1. **`interior-design-advisor`** — all space planning, materials, lighting, budget phasing; never invent exact dims from photos.
2. **`visualise`** — dimensioned SVG floor plans, comparison boards, lighting/zone diagrams (no network fetches; keep fragments iframe-safe).
3. **`GenerateImage`** — photorealistic *concept* stills from structured prompts (style, room, materials, lighting, camera). Always mark conceptual.
4. **`cursor-ide-browser`** — live product research (Century, Birla Opus, local vendors); screenshot + cite URLs/dims/prices.
5. **Built-in shell/files** — write deliverables under `FINAL_DELIVERABLE/`; reuse project PDFs/OCR under `interior_dimension_control/` and `_qa_geometry_review/`.

**Optional later (same agents, no install):** `frontend-skill` / `design-taste-frontend` if packaging a web presentation; Cursor `canvas` for interactive budget/comparison artifacts (not required for PDF handoff).

---

## Available NOW vs needs install

### Available in this Cursor environment (no install)

| Asset | Path / ID | Notes |
| --- | --- | --- |
| MCP: browser | `cursor-ide-browser` | Navigate, snapshot, screenshot, CDP |
| MCP: app control | `cursor-app-control` | Workspace/project helpers only |
| Skill: interior design | `~/.codex/skills/interior-design-advisor/` | Primary design method |
| Skill: visualise | `~/.codex/skills/visualise/` | SVG/HTML inline visuals |
| Skill: Figma | `~/.codex/skills/figma/` | Docs only until Figma MCP is configured |
| Skill: Figma implement | `~/.codex/skills/figma-implement-design/` | Needs Figma MCP + file URLs |
| Skill: Playwright | `~/.codex/skills/playwright/` | Browser automation for research |
| Skill: frontend / taste | `frontend-skill`, `design-taste-frontend` | Presentation UIs if needed |
| Skill: canvas | `~/.cursor/skills-cursor/canvas/` | Live React side panel (Cursor IDE) |
| Tool: GenerateImage | Agent built-in | Concept imagery |

**Not present in this session’s MCP catalog:** Figma MCP, Blender MCP, architecture-mcp, Homestyler, Planner5D.

### Needs install / account / setup (optional advanced)

| Tool | Setup notes | When to use |
| --- | --- | --- |
| **Blender MCP** ([ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp)) | Install Blender 4.x+, `uvx blender-mcp`, enable Blender addon, add to `.cursor/mcp.json`; run Blender with server listening | True 3D scenes, materials, viewport screenshots |
| **Blender MCP forks** ([harveyxiacn](https://github.com/harveyxiacn/blender-mcp), [blender-mcp-pro](https://github.com/youichi-uda/blender-mcp-pro)) | Same pattern; pro/forks add more tools | Heavier modeling/render pipelines |
| **architecture-mcp** ([npm](https://www.npmjs.com/package/architecture-mcp) / [GitHub](https://github.com/ThomasGorisse/architecture-mcp)) | `npx`/npm MCP config; young package (2026) | Floor plans, palettes, lighting/cost helpers |
| **interior-design-3d-mcp** ([npm](https://www.npmjs.com/package/interior-design-3d-mcp)) | npm MCP; SceneView-oriented | Room planning / AR-style tooling experiments |
| **Figma MCP + Interior Design Kit 3D** | Connect Figma MCP; install [Figma plugin](https://www.figma.com/community/plugin/1630582372899645428/interior-design-kit-3d) | Design-system / moodboard ? code handoff |
| **Planner 5D B2B API** | Enterprise contract only; JS SDK + REST; AI plan recognition | Productized embed / volume recognition — **not for this sprint** |
| **Homestyler Enterprise API/SDK** | Business/enterprise sales; white-label | Same — sales-gated, not agent-ready today |
| **Three.js planners** (BuildSphere, Blueprint3D Modern, Planova, Homemaker) | Clone + run locally (Node) | Custom interactive walkthroughs post-delivery |

---

## Optional advanced 3D (post-delivery)

### Blender + Blender MCP (highest-value upgrade)

```json
{
  "mcpServers": {
    "blender": {
      "command": "uvx",
      "args": ["blender-mcp"]
    }
  }
}
```

1. Install Blender + enable the project’s MCP addon.  
2. Start Blender, start the addon socket server.  
3. Restart Cursor; confirm Tools & MCP.  
4. Use Poly Haven / Sketchfab integrations for furniture HDRIs if available in the chosen fork.  
5. Export GLB for web Three.js viewers later.

**Caveat:** Blocks delivery if treated as required; keep as Phase 2 precision visualization.

### Browser Three.js (no MCP)

- [BuildSphere](https://github.com/amarjaleelbanbhan/BuildSphere) — R3F floor planner, JSON export  
- [Blueprint3D Modern](https://github.com/charmlinn/blueprint3d-modern) — 2D/3D planner, IndexedDB  
- [Planova](https://github.com/XUranus/planova) — plan image ? walkable 3D  
- [Homemaker](https://github.com/bayllama/homemaker) — chat-driven Three.js interiors  

Useful for a future interactive client demo; not needed for PDF/SVG handoff.

### Commercial web tools (manual / browser only)

- Homestyler web / AI Studio — manual UI via browser MCP; **no free public API for agents**  
- Planner 5D — consumer UI free/paid; API is **B2B enterprise only**

---

## Links / sources

| Topic | URL |
| --- | --- |
| Blender MCP (primary) | https://github.com/ahujasid/blender-mcp |
| Blender MCP (extended) | https://github.com/harveyxiacn/blender-mcp |
| Blender MCP Pro | https://github.com/youichi-uda/blender-mcp-pro |
| architecture-mcp | https://www.npmjs.com/package/architecture-mcp |
| interior-design-3d-mcp | https://www.npmjs.com/package/interior-design-3d-mcp |
| mcp-archviz (stub/provider pattern) | https://github.com/Simoagadir95/mcp-archviz |
| Planner 5D B2B API overview | https://support.planner5d.com/en/articles/15189751-planner-5d-b2b-api-technical-overview |
| Planner 5D public API stance | https://support.planner5d.com/en/articles/7245729-is-there-a-public-api-available-for-planner-5d |
| Homestyler business / API | https://www.homestyler.com/pricing/business |
| Figma Interior Design Kit 3D | https://www.figma.com/community/plugin/1630582372899645428/interior-design-kit-3d |
| BuildSphere | https://github.com/amarjaleelbanbhan/BuildSphere |
| Blueprint3D Modern | https://github.com/charmlinn/blueprint3d-modern |
| Planova | https://github.com/XUranus/planova |
| Homemaker | https://github.com/bayllama/homemaker |
| Cursor MCP setup guide | https://www.truefoundry.com/blog/mcp-servers-in-cursor-setup-configuration-and-security-guide |

---

## Decision for Bhadravati

**Ship with:** interior-design-advisor + visualise (SVG plans) + GenerateImage (concepts) + browser MCP (sourcing).  

**Defer:** Blender MCP / architecture-mcp / commercial plan APIs until after client handoff package is locked — they improve fidelity, not unblock delivery.
