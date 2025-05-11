<script>
  import {onMount} from "svelte";
  import {getDrivers} from "../lib/api.js";

  let drivers = [];

  async function fetchDrivers() {
    console.log("fetchDrivers called")
    drivers = await getDrivers();
    console.log("Drivers fetched:", drivers);
  }

  onMount(() => {
    fetchDrivers();
  });
</script>

<ul>
  {#each drivers as driver}
    <li>{driver.driver_name}</li>
    <ul>
      <li>{driver.team_name}</li>
      <li>{driver.driver_number}</li>
    </ul>
  {/each}
</ul>