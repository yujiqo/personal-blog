<script lang="ts">
  import * as Avatar from "$lib/components/ui/avatar/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
  import { badgeVariants } from "$lib/components/ui/badge/index.js";

	import avatar from '$lib/assets/avatar.jpg';
	import bento from '$lib/assets/bento.svg';
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
      <img class="size-5 m-1" src={bento} alt="logo"> Bento (SNS)
    </a>
  </Card.Header>
</Card.Root>
