// Serves the compiled resume at its old URL, /resume/build/resume.pdf.
// GitHub Actions builds it from content/resume/resume.tex.
import { readFile } from "node:fs/promises";

export async function GET() {
  const pdf = await readFile("content/resume/build/resume.pdf");
  return new Response(pdf, { headers: { "Content-Type": "application/pdf" } });
}
