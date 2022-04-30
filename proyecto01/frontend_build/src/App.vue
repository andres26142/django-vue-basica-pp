<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <router-link to="/" class="navbar-brand">
        Proyecto01
      </router-link>
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/clientes" class="nav-link">
            Clientes
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/adicionar" class="nav-link">
            Adicionar
          </router-link>
        </li>
      </div>
    </nav>
    <div class="container mt-3">
      <router-view />
    </div>
  </div>
</template>

<script>
  export default {
    name: "app"
  };
</script>