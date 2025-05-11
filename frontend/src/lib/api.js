export async function getDrivers() {
  try {
    console.log("getDrivers called")
    const response = await fetch(`http://127.0.0.1:8000/drivers`)
    if (!response.ok) throw new Error("Failed to fetch drivers.")
      return await response.json();
  } catch (error) {
    console.error("Error when fetching drivers.", error)
    return [];
  }
}