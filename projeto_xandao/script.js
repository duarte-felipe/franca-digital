document.getElementById('salvar').addEventListener('click', function () {
    // Captura os valores dos campos do formulário
    const nome = document.getElementById('nome').value;
    const endereco = document.getElementById('endereco').value;
    const telefone = document.getElementById('telefone').value;
    const email = document.getElementById('email').value;
    const idade = document.getElementById('idade').value;
    const nota = document.getElementById('nota').value;

    // Atualiza o conteúdo da seção de saída
    const output = document.getElementById('output');
    output.innerHTML = `
        <p><strong>Nome:</strong> ${nome}</p>
        <p><strong>Endereço:</strong> ${endereco}</p>
        <p><strong>Telefone:</strong> ${telefone}</p>
        <p><strong>E-mail:</strong> ${email}</p>
        <p><strong>Idade:</strong> ${idade}</p>
        <p><strong>Nota:</strong> ${nota}</p>
    `;
});