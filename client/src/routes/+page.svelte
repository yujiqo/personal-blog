<script lang="ts">
  import { toggleMode } from "mode-watcher";

  import * as Avatar from "$lib/components/ui/avatar/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
  import * as Dialog from "$lib/components/ui/dialog/index.js";
  import * as Field from "$lib/components/ui/field/index.js";
  import { Badge, badgeVariants } from "$lib/components/ui/badge/index.js";
  import { Button, buttonVariants } from "$lib/components/ui/button/index.js";
  import { Input } from "$lib/components/ui/input/index.js";

  import SunIcon from "@lucide/svelte/icons/sun";
  import MoonIcon from "@lucide/svelte/icons/moon";
	import avatar from "$lib/assets/avatar.jpg";
	import bento from "$lib/assets/bento.svg";

  import type { PageProps } from "./$types";


  let { data }: PageProps = $props();
  let posts = $derived(data.posts);

  let options: Intl.DateTimeFormatOptions = {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit"
  };

  let text = $state("");
  let file: File | null;

  async function handleSubmit() {
    const closeBtn = document.querySelector("button[data-dialog-close]") as HTMLButtonElement;

    closeBtn.click();

    const formData = new FormData();

    formData.append("text", text);
    if (file) formData.append("fileobj", file);

    await fetch("http://127.0.0.1:8000/posts/", {
      method: "post",
      body: formData
    });

    text = "";
    file = null;

    const response = await fetch("http://127.0.0.1:8000/posts/");

    posts = await response.json();
  }
</script>

<Card.Root>
  <Card.Header class="flex justify-between items-center">
    <div class="flex items-center">
      <Avatar.Root class="mr-3">
        <Avatar.Image src={avatar} alt="@yujiqo" />
        <Avatar.Fallback>YJQ</Avatar.Fallback>
      </Avatar.Root>
      <Card.Title class="mr-3">@<span class="underline">yujiqo</span>'s personal blog</Card.Title>
      <a href="https://bento.me/yujiqo" class={badgeVariants({ variant: "default" })} target="_blank">
        <img class="size-5" src={bento} alt="logo">
        Bento (SNS)
      </a>
    </div>
    <Button onclick={toggleMode} variant="outline" size="icon">
      <SunIcon
        class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 !transition-all dark:-rotate-90 dark:scale-0"
      />
      <MoonIcon
        class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 !transition-all dark:rotate-0 dark:scale-100"
      />
      <span class="sr-only">Toggle theme</span>
    </Button>
  </Card.Header>
  <Card.Footer>
    <Dialog.Root>
      <Dialog.Trigger class={buttonVariants({ variant: "default" }) + " w-1/1"}>Post</Dialog.Trigger>
      <Dialog.Content class="sm:max-w-[425px]">
        <Dialog.Header class="mb-3">
          <Dialog.Title>Create Post</Dialog.Title>
        </Dialog.Header>
        <Field.Set>
          <Field.Group>
            <Field.Field>
              <Field.Label for="text">Text</Field.Label>
              <Input id="text" type="text" bind:value={text} placeholder="Enter the post's text" />
            </Field.Field>
            <Field.Field>
              <Field.Label for="media">Media</Field.Label>
              <Input
                id="media"
                type="file"
                onchange={(event: Event) => {
                  const target = event.currentTarget as HTMLInputElement;

                  file = target.files?.[0] ?? null;
                }}
              />
            </Field.Field>
          </Field.Group>
        </Field.Set>
        <Dialog.Footer>
          <Button onclick={handleSubmit}>Post</Button>
        </Dialog.Footer>
      </Dialog.Content>
    </Dialog.Root>
  </Card.Footer>
</Card.Root>

{#each posts as post }
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
