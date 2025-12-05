<script lang="ts">
  import * as Avatar from "$lib/components/ui/avatar/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
  import { Badge, badgeVariants } from "$lib/components/ui/badge/index.js";

	import avatar from '$lib/assets/avatar.jpg';
	import bento from '$lib/assets/bento.svg';

  import type { PageProps } from "./$types";

  let { data }: PageProps = $props();

  let options: Intl.DateTimeFormatOptions = {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  };
</script>

<Card.Root>
  <Card.Header class="flex justify-between items-center">
    <div class="flex items-center">
      <Avatar.Root class="mr-3">
        <Avatar.Image src={avatar} alt="@yujiqo" />
        <Avatar.Fallback>YJQ</Avatar.Fallback>
      </Avatar.Root>
      <Card.Title>@yujiqo's personal blog</Card.Title>
    </div>
    <a href="https://bento.me/yujiqo" class={badgeVariants({ variant: "default" })} target="_blank">
      <img class="size-5 m-1" src={bento} alt="logo">
      Bento (SNS)
    </a>
  </Card.Header>
</Card.Root>
{#each data.posts as post }
  <Card.Root class={"mt-3" + (post.filepath ? " pt-0" : "") }>
    {#if post.filetype === "photo"}
      <img class="rounded-t-lg" src={"http://127.0.0.1:8000/" + post.filepath} alt="post_photo">
    {:else if post.filetype === "video"}
      <video class="rounded-t-lg" controls>
        <source src={"http://127.0.0.1:8000/" + post.filepath} />
        <track kind="captions" src="" srclang="en" label="English" default>
      </video>
    {/if}
    <Card.Content>
      <p>{post.text}</p>
      <Card.Description class="text-right">
        <Badge variant="secondary">{new Date(post.updated_at).toLocaleString("en-US", options)}</Badge>
      </Card.Description>
    </Card.Content>
  </Card.Root>
{/each}
