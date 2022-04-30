<template>
    <div class="submit-form">
        <div v-if="!enviar">
            <div class="form-group">
                <label for="nom_cliente">
                    Nombre
                </label>
                <input
                    type="text"
                    class="form-control"
                    id="nom_cliente"
                    required
                    v-model="cliente.nom_cliente"
                    name="nom_cliente"
                />
            </div>

            <div class="form-group">
                <label for="estado">
                    Estado
                </label>
                <input
                    type="text"
                    class="form-control"
                    id="estado"
                    required
                    v-model="cliente.estado"
                    name="estado"
                />
            </div>

            <button @click="guardarCliente" class="btn btn-success">
                Enviar
            </button>
        </div>

        <div v-else>
            <h4>
                Ha enviado la solicitud con exito.
            </h4>
            <button class="btn btn-success" @click="nuevoCliente">
                Adicionar
            </button>
        </div>

    </div>

</template>

<script>
    import ClienteServicioDatos from "../services/ClienteServicioDatos";

    export default {
        name: "adicionar-cliente",
        data() {
            return {
                cliente: {
                    id: null,
                    nom_cliente: "",
                    estado: ""
                },
                enviar: false
            };
        },

        methods: {
            guardarCliente() {
                var datos = {
                    nom_cliente: this.cliente.nom_cliente,
                    estado: this.cliente.estado
                };
                ClienteServicioDatos.crear(datos)
                    .then(response => {
                        this.cliente.id = response.data.id;
                        console.log(response.data);
                        this.enviar = true;
                    })
                    .catch(e => {
                        console.log(e);
                    });
            },

            nuevoCliente() {
                this.enviar = false;
                this.cliente = {};
            }
        }
    };

</script>

<style>
    .submit-form {
        max-width: 300px;
        margin: auto;
    }
</style>