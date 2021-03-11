<!-- https://svelte.dev/tutorial/await-blocks -->
<script>
  async function getNumber() {
    //https://stackoverflow.com/a/62664247/13040423
    const res = await fetch(`http://localhost:4000/get/1/`);
    const text = await res.text();

    if (res.ok) {
      return text;
    } else {
      throw new Error(text);
    }
  }
  // https://blog.csdn.net/qq_36183935/article/details/80570062
  let promise = getNumber();
</script>

<h2>GET</h2>
<button
  on:click={() => {
    promise = getNumber();
  }}
>
  generate random number
</button>

{#await promise}
  <p>...waiting</p>
{:then number}
  <p>The number is {number}</p>
{:catch error}
  <p style="color: red">{error.message}</p>
{/await}
