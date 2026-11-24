import { existsSync, readdirSync } from "node:fs";
import { getCollection, type CollectionEntry } from "astro:content";

export type Project = CollectionEntry<"projects">;

export const statusLabels = {
  "wip-private": "In progress · private for now",
  wip: "In progress",
  private: "Private repo",
} as const;

// Base URL of the R2 bucket that serves explainer videos. Cloudflare Pages
// ignores Range requests, and iOS Safari won't play video without them.
// Upload with tools/upload-media.sh after rendering.
export const mediaBase = "https://media.tahmidul612.com";

// Projects with an explainer video in their bundle get a "Video" badge.
// Read from disk (the build runs in Node) so the MP4s stay out of the output.
export const hasVideo = (p: Project) => {
  const dir = `content/projects/${p.id}`;
  return existsSync(dir) && readdirSync(dir).some((f) => f.endsWith(".mp4"));
};

export async function projectsIn(group: Project["data"]["group"]) {
  const all = await getCollection("projects", (p) => p.data.group === group);
  return all.sort((a, b) => a.data.weight - b.data.weight);
}
