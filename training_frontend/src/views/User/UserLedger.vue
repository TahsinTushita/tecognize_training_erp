<template>
  <h1 class="pt-10 text-xl font-semibold">User Ledger</h1>
  <table class="m-10">
    <thead>
      <tr>
        <th class="w-1/5 px-4 py-4 text-center border-2">ID</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">User Name</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Phone</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Batch</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Paid</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Due</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Profit</th>
      </tr>
    </thead>
    <!-- <tbody v-if="styles.length">
            <tr v-for="style in styles" :key="style.style">
              <td class="w-1/5 px-4 py-4 text-center">{{ style.name }}</td>
              <td class="w-1/5 px-4 py-4 text-center">{{ style.colour }}</td>
              <td class="w-1/5 px-4 py-4 text-center">{{ style.sz }}</td>
              <td class="w-1/5 px-4 py-4 text-center">{{ style.price }}</td>
              <td class="w-1/5 px-4 py-4 text-center">{{ style.style }}</td>
              <td class="w-1/5 px-4 py-4 text-center">{{ style.stock }}</td>
            </tr>
          </tbody> -->
  </table>
</template>