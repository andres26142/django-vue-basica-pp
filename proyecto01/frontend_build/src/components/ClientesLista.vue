<template>
    <div class="list row">
        <div class="col-md-8">
            <div class="input-group mb-3">
                <input
                    type="text"
                    class="form-control"
                    placeholder="Buscar por estado"
                    v-model="estado"
                />
                <div class="input-group-append">
                    <button class="btn btn-outline-secondary" type="button" @click="buscarEstado">
                        Buscar
                    </button>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <h4>
                Lista de Clientes
            </h4>
            <ul class="list-group">
                <li
                    class="list-group-item"
                    :class="{ active: index == indexActual }"
                    v-for="(cliente, index) in clientes"
                    :key="index"
                    @click="establecerClienteActivo(cliente, index)"
                >
                    {{ cliente.nom_cliente }}
                </li>
            </ul>
        </div>
        <div class="col-md-6">
            <div v-if="clienteActual">
                <h4>
                    Cliente
                </h4>
                <div>
                    <label>
                        <strong>
                            Nombre:
                        </strong>
                    </label>
                    {{ clienteActual.nom_cliente }}
                </div>
                <div>
                    <label>
                        <strong>
                            Estado:
                        </strong>
                    </label>
                    {{ clienteActual.estado }}
                </div>

                <router-link :to="'/clientes/' + clienteActual.id" class="badge badge-warning">
                    Modificar
                </router-link>
            </div>

            <div v-else>
                <br />
                <p>
                    Dar clic en un cliente...
                </p>
            </div>
        </div>
        
    </div>
</template>

<script>
    import ClienteServicioDatos from "../services/ClienteServicioDatos";
    export default {
        name: "clientes-lista",
        data() {
            return {
                clientes: [],
                clienteActual: null,
                indexActual: -1,
                estado: ""
            };
        },

        methods: {
            recuperarCliente() {
                ClienteServicioDatos.ObtenerTodo()
                .then(Response => {
                    this.clientes = Response.data;
                    console.log(Response.data);
                })
                .catch(e => {
                    console.log(e);
                });
            },

            actualizarLista() {
                this.clienteActual = null;
                this.indexActual = -1;
            },

            establecerClienteActivo(cliente, index) {
                this.clienteActual = cliente;
                this.indexActual = cliente ? index : -1;
            },

            buscarEstado () {
                ClienteServicioDatos.buscarPorEstado(this.estado)
                .then(Response => {
                    this.clientes = Response.data;
                    this.establecerClienteActivo(null);
                    console.log(Response.data);
                })
                .catch(e => {
                    console.log(e)
                });
            }
        },

        mounted() {
            this.recuperarCliente();
        }
    };

</script>

<style>
    .list {
        text-align: left;
        max-width: 750 px;
        margin: auto;
    }
</style>