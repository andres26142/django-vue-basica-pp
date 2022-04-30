<template>
    <div v-if="clienteActual" class="edit-form">
        <h4>
            Cliente
        </h4>
        <form>
            <div class="form-grup">
                <label for="nom_cliente">
                    Nombre
                </label>
                <input
                    type="text"
                    class="form-control"
                    id="nom_cliente"
                    v-model="clienteActual.nom_cliente"
                />
            </div>

            <div class="form-group">
                <label form="estado">
                    Estado
                </label>
                <input
                    type="text"
                    class="form-control"
                    id="estado"
                    v-model="clienteActual.estado"
                />
            </div>
        </form>

        <button class="badge badge-danger mr-2" @click="eliminarCliente">
            Eliminar
        </button>

        <button type="submit" class="badge badge-sucess" @click="actualizarCliente">
            Actualizar
        </button>

        <p>
            {{ mensaje }}
        </p>

    </div>

    <div v-else>
        <br>
        <p>
            Click en un cliente...
        </p>
    </div>

</template>

<script>
    import ClienteServicioDatos from "../services/ClienteServicioDatos";
    export default {
        name: "unCliente",

        data() {
            return {
                clienteActual: null, 
                mensaje: ''
            };
        },
        methods: {
            obtenerCliente(id) {
                ClienteServicioDatos.obtener(id)
                    .then(Response => {
                        this.clienteActual = Response.data;
                        console.log(Response.data);
                    })
                    .catch(e => {
                        console.log(e);
                    });
            },
            actualizarCliente() {
                ClienteServicioDatos.actualizar(this.clienteActual.id, this.clienteActual)
                    .then(Response => {
                        console.log(Response.data);
                        this.mensaje = "El cliente se ha actualizado";
                    })
                    .catch(e => {
                        console.log(e);
                    });
            },
            eliminarCliente() {
                ClienteServicioDatos.eliminar(this.clienteActual.id)
                    .then(Response => {
                        console.log(Response.data);
                        this.$router.push({ 
                            name: "clientes" 
                            });
                    })
                    .catch(e => {
                        console.log(e);
                    });
                }
            },
        mounted() {
            this.mensaje = '';
            this.obtenerCliente(this.$route.params.id);
        }
    };
</script>

<style>
    .edit-form {
        max-width: 300px;
        margin: auto;
    }
</style>