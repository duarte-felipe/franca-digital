let clientes = [];

function cadastrarCliente() {
    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const telefone = document.getElementById("telefone").value;

    const novoCliente = {
        nome,
        email,
        telefone
    };

    clientes.push(novoCliente);
    exibirClientes();
}

function exibirClientes() {
    const listaClientes = document.getElementById('clientesList');
    listaClientes.innerHTML = "";  // limpei a lista antes de adicionar os novos clientes

    clientes.forEach((cliente) => {
        const item = document.createElement('li');
        item.textContent = `Nome: ${cliente.nome} | Email: ${cliente.email} | Telefone: ${cliente.telefone}`;
        listaClientes.appendChild(item);
    });
}
