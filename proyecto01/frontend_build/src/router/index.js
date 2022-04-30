import { createWebHistory, createRouter } from "vue-router";

const routes = [
    {
        path: "/",
        alias: "/clientes",
        name: "clientes",
        component: () => import("../components/ClientesLista.vue")
    },
    {
        path: "/clientes/:id",
        name: "cliente-detalle",
        component: () => import("../components/Cliente.vue")
    },
    {
        path: "/adicionar",
        name: "adicionar",
        component: () => import("../components/AdicionarCliente.vue")
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;