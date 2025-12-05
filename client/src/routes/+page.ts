import type { PageLoad } from "./$types"


export const load: PageLoad = async ({ fetch }) => {
  const response = await fetch("http://127.0.0.1:8000/posts/");
  const posts = await response.json();

  return { posts };
};
