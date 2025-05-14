# Comunicação entre Servidores Django com Docker

Este projeto demonstra como realizar o envio de requisições HTTP entre múltiplos servidores Django, cada um rodando em seu próprio container Docker.

## 🟢 Subindo todos os servidores na mesma máquina

Para iniciar todos os servidores ao mesmo tempo:

```bash
docker-compose up --build
```

## 🔁 Subindo servidores individualmente

Para iniciar apenas um servidor específico (em uma máquina distinta, por exemplo):

1. Acesse o diretório que contém o `Dockerfile` do servidor desejado
2. Execute o comando:

```bash
docker-compose up --build <nome_do_container>
```

### Exemplo:

```bash
docker-compose up --build servidor1
```

## ❌ Removendo containers, volumes e imagens

Para parar e remover todos os containers, volumes e imagens associadas:

```bash
docker-compose down --volumes --rmi all
```

---

✅ Com isso, você pode distribuir cada servidor em diferentes máquinas e testar a comunicação entre eles via rede local.
