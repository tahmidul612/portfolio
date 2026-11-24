// @ts-check
import { defineConfig, fontProviders } from "astro/config";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://tahmidul612.com",
  // static/ holds files served as-is: favicons, _headers, _redirects, the
  // vCard and the self-contained demos under static/demos/.
  publicDir: "./static",
  integrations: [mdx(), sitemap()],
  // Start fetching a page when a link is hovered or tapped, so moving
  // between pages feels instant.
  prefetch: { prefetchAll: true, defaultStrategy: "hover" },
  vite: {
    build: {
      // Keep caption files as real files: <track> needs a URL, not a data: URI.
      assetsInlineLimit: (file) => (file.endsWith(".vtt") ? false : undefined),
    },
  },
  image: {
    responsiveStyles: true,
    layout: "constrained",
  },
  fonts: [
    {
      name: "Unbounded",
      cssVariable: "--font-display",
      provider: fontProviders.google(),
      weights: [400, 500],
      styles: ["normal"],
      subsets: ["latin"],
      fallbacks: ["system-ui", "sans-serif"],
    },
    {
      name: "Onest",
      cssVariable: "--font-body",
      provider: fontProviders.google(),
      weights: [400, 500, 600],
      styles: ["normal"],
      subsets: ["latin"],
      fallbacks: ["system-ui", "sans-serif"],
    },
  ],
});
