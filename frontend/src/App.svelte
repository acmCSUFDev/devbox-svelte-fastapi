<script lang="ts">
  import { baseURL } from "./lib/api";

  let message = "Change me!";
  let duration = "";
  $: promise = echo(message);

  async function echo(message: string): Promise<unknown> {
    const nowMs = Date.now();
    try {
      const response = await fetch(baseURL + "/api/echo", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
      });
      if (!response.ok) {
        throw new Error("Server responded with status " + response.status);
      }
      return await response.json();
    } finally {
      duration = `${Date.now() - nowMs}ms`;
    }
  }
</script>

<main class="container">
  <nav>
    <ul>
      <li><strong>Devbox Demo</strong></li>
    </ul>
  </nav>

  <h1>Echo</h1>

  <form>
    <label for="message">
      Try changing the input below to see the server response:
    </label>
    <input bind:value={message} id="message" />
  </form>

  <div>
    <p>
      Output:
      {#if duration}
        <span style="color: var(--pico-muted-color)">(took {duration})</span>
      {/if}
    </p>

    {#await promise}
      <pre><code>...</code></pre>
    {:then echoedMessage}
      <pre><code>{JSON.stringify(echoedMessage, null, 2)}</code></pre>
    {:catch error}
      <p style="color: red">error: <code>{error.message}</code></p>
    {/await}
  </div>
</main>
