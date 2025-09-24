# Insights e Anotações Pessoais: Desafio prático com Lambda + S3 no Bootcamp Code Girls 2025

Oi! Eu sou Anny Karoline, e esse arquivo é tipo um "diário de bordo" do meu desafio prático com AWS Lambda e S3. Assisti todas as vídeo-aulas e agora anotei o que rolou durante a criação do desafio prático. #CodeGirls2025 #WomenInTech

## Conceitos Chave que Fixei das Aulas
Nas aulas, o que mais me marcou foi a ideia de **serverless como liberdade**. Lambda roda código sem gerenciar infra (paga só pelo uso, 1 milhão de requests grátis por mês no Free Tier), e S3 é o "armazém infinito" com eventos que disparam ações automáticas. Algumas das explicações sobre:
- **Handlers e Runtimes:** O `lambda_handler(event, context)` é o coração – recebe eventos do S3 (como "ObjectCreated") e processa. Escolhi Python 3.12 porque é familiar e boto3 (SDK AWS) facilita chamadas como `s3.list_objects_v2()`.
- **Triggers e Eventos:** S3 notifica Lambda via configurações simples (ex.: upload de foto → redimensionar automaticamente).
- **IAM e Segurança:** Roles são cruciais! A trust policy permite que Lambda "assuma" permissões, e policies como AWSLambdaBasicExecutionRole (para logs) + AmazonS3FullAccess (para ler buckets) evitam erros de acesso.
- **CloudWatch:** Logs automáticos para debug – muito bom ver métricas de duração e erros em tempo real.

Esses conceitos saíram do papel pro prático: Meu desafio simula um cenário real, como processar documentos no Santander (ex.: upload de contrato → log e validação automática).

## Minha Experiência: O Que Eu Fiz Passo a Passo
 Criei tudo no console AWS (us-east-1, Free Tier) em cerca de 25 minutos:
- **S3 Bucket:** Nomeei `bucket-lambda-codegirls2025`. Bloqueei acesso público e fiz 'upload de um arquivo .txt teste com "Primeiro upload serverless!".
- **IAM Role:** Criei `role-lambda-s3-automatizada` e anexei as policies.
- **Lambda Function:** Nome `lambda-s3-trigger`. Copiei o código Python das aulas, adaptando pra listar objetos. Veja `lambda-code.py` neste repo.
- **Trigger**: Adicionei S3 como source, evento "All object create" 
- **Teste**: Upload no S3 → CloudWatch logs mostraram minha mensagem customizada.
  
## Aprendizados Pessoais e Reflexões
Aqui vão minhas reflexões reais após o desafio prático:

### Técnico
Serverless é um **game-changer** – Lambda + S3 cria fluxos **zero-ops**, ideal pra apps escaláveis. Aprendi que eventos S3 são **assíncronos** (não bloqueiam uploads), e **boto3** é super intuitivo (como uma extensão do Python que uso em projetos pessoais). No meu código, o `list_objects_v2()` rodou em milissegundos, provando como automação serverless escala sem esforço.

### Carreira
Com Lambda, eu foco em **lógica** (ex.: processar dados de clientes no Santander sem infra headache).

### Impacto no Bootcamp
As aulas foram **cruciais**; sem elas, eu pularia IAM e quebraria tudo. Futuro: Quero estender pra **API Gateway** (webhooks) ou **Step Functions** (orquestração).

## Dicas para Quem Vem Depois (Minhas Anotações Práticas)

- **Setup Rápido:** Sempre crie a **role IAM primeiro** – evita idas e vindas no console. Eu fiz isso e o deploy fluiu liso.
- **Debug Ninja:** Use **CloudWatch Logs Insights** pra filtrar erros (ex.: query por *"AccessDenied"*). Teste Lambda isolada com **eventos mock** na aba "Test".
- **Boas Práticas:** Use **variáveis de ambiente** pro bucket name (não hardcode); monitore quotas Free Tier (**1M requests** grátis). Pra prod, adicione **dead-letter queues** pra falhas.

>Essa doc me ajuda a revisar para certificações (ex.: AWS Developer Associate).
