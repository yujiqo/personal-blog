<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.ico';

  import { ModeWatcher } from "mode-watcher";

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<ModeWatcher />
<div class="w-2/5 m-auto my-10">
  {@render children()}
</div>
