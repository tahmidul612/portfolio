import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

// One page bundle per project: content/projects/<slug>/index.mdx, with its
// images, posters and captions next to it. The folder name is the URL slug.
const projects = defineCollection({
  loader: glob({
    pattern: "*/index.mdx",
    base: "./content/projects",
    generateId: ({ entry }) => entry.split("/")[0],
  }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      // The card text on the overview.
      summary: z.string().optional(),
      // work and personal get their own pages; smaller renders inline at the
      // bottom of the overview.
      group: z.enum(["work", "personal", "smaller"]),
      // Lower comes first within a group.
      weight: z.number(),
      // Work entries: when it ran, shown next to the title.
      period: z.string().optional(),
      // Shown on the home page under "Selected projects".
      featured: z.boolean().default(false),
      status: z.enum(["wip-private", "wip", "private"]).optional(),
      demo: z.boolean().default(false),
      // Card image. Projects with one are shown large on the overview.
      thumbnail: image().optional(),
      thumbnailAlt: z.string().optional(),
      links: z.array(z.object({ label: z.string(), url: z.url() })).default([]),
      tech: z.array(z.string()).default([]),
      // The projects used to be one long page; /projects/#<oldAnchor> still
      // lands on this project.
      oldAnchor: z.string().optional(),
    }),
});

export const collections = { projects };
