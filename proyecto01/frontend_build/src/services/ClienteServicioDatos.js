import http from "../api";

class ClienteServicioDatos {
    ObtenerTodo() {
        return http.get("/cliente/");
    }

    obtener(id) {
        return http.get(`/cliente/${id}/`);
    }

    crear(datos) {
        return http.post("/cliente/", datos);
    }

    actualizar(id, datos) {
        return http.put(`/cliente/${id}/`, datos);
    }

    eliminar(id) {
        return http.delete(`/cliente/${id}/`);
    }

    buscarPorEstado(estado) {
        return http.get(`/cliente?estado=${estado}`);
    }
}

export default new ClienteServicioDatos();