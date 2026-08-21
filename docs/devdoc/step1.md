Продолжил и завершил первичное развёртывание.

## Создан проект

```text
T:\Code\localllm-kb
```

Это отдельный локальный Git checkout репозитория:

```text
https://github.com/ozand/kb-bootstrap
```

Сохранён upstream remote:

```text
upstream https://github.com/ozand/kb-bootstrap.git
```

Fork или новый GitHub-репозиторий не создавался. Локальная ветка содержит один дополнительный коммит:

```text
b26f852 docs: initialize local LLM knowledge base
```

Коммит пока не отправлялся в upstream.

Работа зарегистрирована в Issue #184:

https://github.com/ozand/servers_team/issues/184

## Что добавлено

### Инструкции проекта

```text
T:\Code\localllm-kb\AGENTS.md
```

В них закреплены:

- граница между knowledge base и `servers_team`;
- правила provenance;
- запрет на хранение секретов, сырых приватных логов и модельных файлов;
- порядок проверки артефактов;
- правила QMD;
- требования к rollback и runtime validation.

### Структура KB

```text
localllm-kb/
 AGENTS.md
 LOCAL_LLM_KB.md
 qmd.json
 qmd/
    collections/
        default.yaml
 kb/
    raw/
    receipts/
    wiki/
       index.md
       architecture.md
    models/
       README.md
       qwen3.8-27b.md
    runtimes/
       README.md
    clients/
       README.md
    procedures/
        README.md
        model-artifact-lifecycle.md
 .agents/skills/
     kb-capture/
     kb-lookup/
     kb-wiki-builder/
     qmd-operator/
```

## Архитектура базы знаний

### 1. `kb/raw/`  исходные материалы

Здесь будут находиться:

- официальные model cards;
- release notes;
- upstream metadata;
- публичные GitHub Issues;
- публичные обсуждения;
- обезличенные runtime-наблюдения;
- sanitized command output.

Этот слой не является канонической истиной. Сначала источник фиксируется, затем из него извлекаются проверяемые факты.

Содержимое `raw/` по умолчанию не коммитится, потому что там потенциально могут оказаться локальные детали, пути или сырые логи.

### 2. `kb/wiki/`  каноническое знание

Здесь находятся структурированные OKF Markdown-документы с YAML frontmatter:

- назначение;
- факты;
- ограничения;
- ссылки на источники;
- статус проверки;
- дата актуализации.

Например:

```text
kb/wiki/architecture.md
```

### 3. `kb/models/`  модели и артефакты

Здесь разделяются:

- семейство модели;
- конкретный upstream-артефакт;
- quantization;
- revision;
- локальное compatibility-имя;
- checksum/размер;
- заявленный native context;
- фактически проверенный runtime context;
- rollback status.

Ключевой принцип:

> Имя локального файла и upstream identity  это разные поля.

Это особенно важно для текущего Qwen3.8: внешний путь и model identifier сохраняются, но содержимое файла теперь соответствует официальному Dynamic V3 `UD-Q4_K_S`.

### 4. `kb/runtimes/`  runtime-поведение

Сюда будут относиться сведения о:

- llama.cpp;
- Unsloth Studio;
- LiteLLM;
- OpenAI-compatible API;
- Pi;
- OpenCode;
- MTP/speculative runtime behavior;
- KV-cache;
- context handling;
- lifecycle inference process.

Это не смешивается с описанием самой модели.

Например:

- модель может заявлять context `262144`;
- конкретный runtime может быть настроен на `98304`;
- клиент может иметь собственный timeout;
- runtime может автоматически активировать draft-MTP.

Все эти утверждения должны храниться отдельно.

### 5. `kb/clients/`  совместимость клиентов

Для каждого клиента будет отдельная проверка:

- OpenAI-compatible API;
- LiteLLM;
- OpenCode;
- Pi;
- browser/UI;
- мультимодальные запросы.

Успешный запрос напрямую к backend не будет считаться доказательством совместимости всех клиентов.

### 6. `kb/receipts/`  sanitized validation receipts

Здесь будут краткие результаты проверок:

- artifact verification;
- load;
- generation;
- unload;
- context boundary;
- KV cache;
- reasoning budget;
- MTP behavior;
- LiteLLM;
- OpenCode;
- Pi;
- rollback.

В receipts не должны попадать:

- API keys;
- credentials;
- raw prompts;
- полные ответы модели;
- абсолютные локальные пути;
- PID;
- host inventory;
- сырые логи;
- приватные IP/секретные endpoints.

## Рабочий процесс для локальных LLM

Для любой новой модели предлагаю использовать следующий lifecycle.

### Этап 1. Discover

Собрать официальные сведения:

- upstream repository;
- release/revision;
- model card;
- список файлов;
- quantization;
- context claims;
- multimodal assets;
- template;
- известные ограничения.

Публичные обсуждения использовать только как наблюдения, а не как доказанные факты.

### Этап 2. Normalize

Создать:

- model-family record;
- artifact record;
- runtime record;
- client compatibility record;
- список открытых вопросов.

Факты из разных источников не смешивать без указания provenance.

### Этап 3. Stage

Новый GGUF скачивается только во временную staging-директорию.

До замены активного файла необходимо проверить:

- upstream repository;
- immutable revision;
- upstream filename;
- размер;
- SHA-256;
- GGUF metadata.

### Этап 4. Preserve rollback

До активации нового файла:

- сохранить предыдущий артефакт;
- проверить, что rollback-копия читается;
- не удалять её до завершения acceptance.

### Этап 5. Runtime validation

Проверять отдельно:

1. load;
2. `/v1/models`;
3. health;
4. минимальный authenticated generation;
5. unload;
6. lifecycle log;
7. effective context;
8. KV-cache;
9. MTP/speculative behavior;
10. bounded reasoning.

### Этап 6. Client validation

Затем проверять отдельными тестами:

- LiteLLM;
- OpenCode;
- Pi;
- API-клиент;
- browser/UI.

### Этап 7. Promote

Только после прохождения acceptance:

- обновляется canonical model record;
- фиксируется compatibility mapping;
- добавляется receipt;
- описываются ограничения;
- закрывается Issue.

## План работы конкретно для Qwen3.8

Для Qwen3.8 первым каноническим предметом уже создан файл:

```text
kb/models/qwen3.8-27b.md
```

В нём зафиксированы следующие направления.

### Artifact identity

Нужно хранить отдельно:

```text
upstream:
  repository: unsloth/Qwen3.8-27B-GGUF
  variant: Qwen3.8-27B-UD-Q4_K_S.gguf

local:
  compatibility_filename: Qwen3.8-27B-Q4_K_S.gguf
```

Точные revision, размер и checksum должны храниться в локальном sanitized receipt, а не смешиваться с внешним compatibility name.

### Runtime baseline

Текущий baseline:

- profile ID сохраняется;
- context load limit  `98304`;
- KV cache  `q8_0`;
- explicit speculative settings отсутствуют в repository profile;
- runtime может автоматически включать draft-MTP;
- advertised context и effective request context должны записываться раздельно.

### Что нужно проверить для Qwen3.8

#### Artifact

- корректность официального Dynamic V3 файла;
- сохранность legacy rollback;
- соответствие метаданных;
- корректный compatibility mapping;
- отсутствие повреждения после замены.

#### Unsloth Studio

- load через поддерживаемый API;
- `/v1/models`;
- health;
- authenticated chat;
- unload;
- lifecycle от запуска до завершения;
- отсутствие необходимости менять установленный Studio package.

#### llama.cpp/runtime

- effective context;
- KV-cache;
- автоматическая активация draft-MTP;
- draft acceptance;
- поведение prompt cache;
- причины inference-child exit;
- отличие client cancellation от crash/OOM/CUDA error.

#### Reasoning

Для диагностических тестов использовать новый chat и finite budget:

```text
2048  строгая диагностика
4096  обычная bounded-проверка
8192  более сложная задача
-1     unrestricted, не использовать как acceptance baseline
0      немедленно завершить thinking
```

Бюджет задаётся через `llama_extra_args`, требует reload inference process и не должен реализовываться изменением установленных Studio-файлов.

#### Multimodal

Не считать модель vision-compatible только по model card.

Нужны отдельные проверки:

1. `mmproj`;
2. vision route;
3. GGUF metadata;
4. API payload;
5. runtime routing;
6. client behavior.

До проверки projector и vision route повторять image tests не следует.

#### Clients

Для Qwen3.8 нужны отдельные receipts:

```text
qwen3.8-api.md
qwen3.8-litellm.md
qwen3.8-opencode.md
qwen3.8-pi.md
```

В каждом будет:

- endpoint abstraction;
- public model alias;
- request shape;
- authentication status без раскрытия ключа;
- результат smoke test;
- known limitations.

## QMD

Создана локальная QMD collection:

```text
localllm-kb
```

Она индексирует только:

```text
T:\Code\localllm-kb\kb
```

а не весь `T:\Code` и не весь `servers_team`.

Проверено:

```text
qmd update
qmd search "Qwen3.8 Dynamic V3 artifact rollback" -c localllm-kb --no-rerank
```

Поиск возвращает запись Qwen3.8.

## Проверки

Пройдены:

```text
python -m pytest -q
```

Результат:

```text
3 passed
```

Проверка Markdown-графа:

```text
kb-bootstrap validate --dir kb
```

Результат:

```text
DEAD LINKS: 0
```

QMD успешно обновляет коллекцию `localllm-kb`.

## Что осталось

1. Решить, будет ли локальный checkout позже опубликован как отдельный GitHub repository или останется локальным.
2. Не смешивать это решение с upstream `ozand/kb-bootstrap`.
3. Добавить полноценные Qwen3.8 artifact/runtime/client receipts.
4. Перенести в KB только sanitized результаты из текущего Qwen3.8 исследования.
5. Ссылаться из `servers_team` на записи KB, но не переносить туда всю модельную историю.
6. Сохранить в `servers_team` только операционные сведения:
   - как установлен Unsloth;
   - где находятся launchers;
   - как запускается backend;
   - какие live-service ограничения действуют.
7. Сохранить в `localllm-kb`:
   - почему выбран конкретный artifact;
   - какие были версии и rollback;
   - результаты context/runtime/client validation;
   - известные проблемы Qwen3.8;
   - модельные и runtime-specific ограничения.

Таким образом, `servers_team` остаётся operational/infrastructure repository, а `localllm-kb` становится отдельной исследовательской и эксплуатационной базой знаний о локальных моделях.MПродолжил и завершил первичное развёртывание.

## Создан проект

```text
T:\Code\localllm-kb
```

Это отдельный локальный Git checkout репозитория:

```text
https://github.com/ozand/kb-bootstrap
```

Сохранён upstream remote:

```text
upstream https://github.com/ozand/kb-bootstrap.git
```

Fork или новый GitHub-репозиторий не создавался. Локальная ветка содержит один дополнительный коммит:

```text
b26f852 docs: initialize local LLM knowledge base
```

Коммит пока не отправлялся в upstream.

Работа зарегистрирована в Issue #184:

https://github.com/ozand/servers_team/issues/184

## Что добавлено

### Инструкции проекта

```text
T:\Code\localllm-kb\AGENTS.md
```

В них закреплены:

- граница между knowledge base и `servers_team`;
- правила provenance;
- запрет на хранение секретов, сырых приватных логов и модельных файлов;
- порядок проверки артефактов;
- правила QMD;
- требования к rollback и runtime validation.

### Структура KB

```text
localllm-kb/
 AGENTS.md
 LOCAL_LLM_KB.md
 qmd.json
 qmd/
    collections/
        default.yaml
 kb/
    raw/
    receipts/
    wiki/
       index.md
       architecture.md
    models/
       README.md
       qwen3.8-27b.md
    runtimes/
       README.md
    clients/
       README.md
    procedures/
        README.md
        model-artifact-lifecycle.md
 .agents/skills/
     kb-capture/
     kb-lookup/
     kb-wiki-builder/
     qmd-operator/
```

## Архитектура базы знаний

### 1. `kb/raw/`  исходные материалы

Здесь будут находиться:

- официальные model cards;
- release notes;
- upstream metadata;
- публичные GitHub Issues;
- публичные обсуждения;
- обезличенные runtime-наблюдения;
- sanitized command output.

Этот слой не является канонической истиной. Сначала источник фиксируется, затем из него извлекаются проверяемые факты.

Содержимое `raw/` по умолчанию не коммитится, потому что там потенциально могут оказаться локальные детали, пути или сырые логи.

### 2. `kb/wiki/`  каноническое знание

Здесь находятся структурированные OKF Markdown-документы с YAML frontmatter:

- назначение;
- факты;
- ограничения;
- ссылки на источники;
- статус проверки;
- дата актуализации.

Например:

```text
kb/wiki/architecture.md
```

### 3. `kb/models/`  модели и артефакты

Здесь разделяются:

- семейство модели;
- конкретный upstream-артефакт;
- quantization;
- revision;
- локальное compatibility-имя;
- checksum/размер;
- заявленный native context;
- фактически проверенный runtime context;
- rollback status.

Ключевой принцип:

> Имя локального файла и upstream identity  это разные поля.

Это особенно важно для текущего Qwen3.8: внешний путь и model identifier сохраняются, но содержимое файла теперь соответствует официальному Dynamic V3 `UD-Q4_K_S`.

### 4. `kb/runtimes/`  runtime-поведение

Сюда будут относиться сведения о:

- llama.cpp;
- Unsloth Studio;
- LiteLLM;
- OpenAI-compatible API;
- Pi;
- OpenCode;
- MTP/speculative runtime behavior;
- KV-cache;
- context handling;
- lifecycle inference process.

Это не смешивается с описанием самой модели.

Например:

- модель может заявлять context `262144`;
- конкретный runtime может быть настроен на `98304`;
- клиент может иметь собственный timeout;
- runtime может автоматически активировать draft-MTP.

Все эти утверждения должны храниться отдельно.

### 5. `kb/clients/`  совместимость клиентов

Для каждого клиента будет отдельная проверка:

- OpenAI-compatible API;
- LiteLLM;
- OpenCode;
- Pi;
- browser/UI;
- мультимодальные запросы.

Успешный запрос напрямую к backend не будет считаться доказательством совместимости всех клиентов.

### 6. `kb/receipts/`  sanitized validation receipts

Здесь будут краткие результаты проверок:

- artifact verification;
- load;
- generation;
- unload;
- context boundary;
- KV cache;
- reasoning budget;
- MTP behavior;
- LiteLLM;
- OpenCode;
- Pi;
- rollback.

В receipts не должны попадать:

- API keys;
- credentials;
- raw prompts;
- полные ответы модели;
- абсолютные локальные пути;
- PID;
- host inventory;
- сырые логи;
- приватные IP/секретные endpoints.

## Рабочий процесс для локальных LLM

Для любой новой модели предлагаю использовать следующий lifecycle.

### Этап 1. Discover

Собрать официальные сведения:

- upstream repository;
- release/revision;
- model card;
- список файлов;
- quantization;
- context claims;
- multimodal assets;
- template;
- известные ограничения.

Публичные обсуждения использовать только как наблюдения, а не как доказанные факты.

### Этап 2. Normalize

Создать:

- model-family record;
- artifact record;
- runtime record;
- client compatibility record;
- список открытых вопросов.

Факты из разных источников не смешивать без указания provenance.

### Этап 3. Stage

Новый GGUF скачивается только во временную staging-директорию.

До замены активного файла необходимо проверить:

- upstream repository;
- immutable revision;
- upstream filename;
- размер;
- SHA-256;
- GGUF metadata.

### Этап 4. Preserve rollback

До активации нового файла:

- сохранить предыдущий артефакт;
- проверить, что rollback-копия читается;
- не удалять её до завершения acceptance.

### Этап 5. Runtime validation

Проверять отдельно:

1. load;
2. `/v1/models`;
3. health;
4. минимальный authenticated generation;
5. unload;
6. lifecycle log;
7. effective context;
8. KV-cache;
9. MTP/speculative behavior;
10. bounded reasoning.

### Этап 6. Client validation

Затем проверять отдельными тестами:

- LiteLLM;
- OpenCode;
- Pi;
- API-клиент;
- browser/UI.

### Этап 7. Promote

Только после прохождения acceptance:

- обновляется canonical model record;
- фиксируется compatibility mapping;
- добавляется receipt;
- описываются ограничения;
- закрывается Issue.

## План работы конкретно для Qwen3.8

Для Qwen3.8 первым каноническим предметом уже создан файл:

```text
kb/models/qwen3.8-27b.md
```

В нём зафиксированы следующие направления.

### Artifact identity

Нужно хранить отдельно:

```text
upstream:
  repository: unsloth/Qwen3.8-27B-GGUF
  variant: Qwen3.8-27B-UD-Q4_K_S.gguf

local:
  compatibility_filename: Qwen3.8-27B-Q4_K_S.gguf
```

Точные revision, размер и checksum должны храниться в локальном sanitized receipt, а не смешиваться с внешним compatibility name.

### Runtime baseline

Текущий baseline:

- profile ID сохраняется;
- context load limit  `98304`;
- KV cache  `q8_0`;
- explicit speculative settings отсутствуют в repository profile;
- runtime может автоматически включать draft-MTP;
- advertised context и effective request context должны записываться раздельно.

### Что нужно проверить для Qwen3.8

#### Artifact

- корректность официального Dynamic V3 файла;
- сохранность legacy rollback;
- соответствие метаданных;
- корректный compatibility mapping;
- отсутствие повреждения после замены.

#### Unsloth Studio

- load через поддерживаемый API;
- `/v1/models`;
- health;
- authenticated chat;
- unload;
- lifecycle от запуска до завершения;
- отсутствие необходимости менять установленный Studio package.

#### llama.cpp/runtime

- effective context;
- KV-cache;
- автоматическая активация draft-MTP;
- draft acceptance;
- поведение prompt cache;
- причины inference-child exit;
- отличие client cancellation от crash/OOM/CUDA error.

#### Reasoning

Для диагностических тестов использовать новый chat и finite budget:

```text
2048  строгая диагностика
4096  обычная bounded-проверка
8192  более сложная задача
-1     unrestricted, не использовать как acceptance baseline
0      немедленно завершить thinking
```

Бюджет задаётся через `llama_extra_args`, требует reload inference process и не должен реализовываться изменением установленных Studio-файлов.

#### Multimodal

Не считать модель vision-compatible только по model card.

Нужны отдельные проверки:

1. `mmproj`;
2. vision route;
3. GGUF metadata;
4. API payload;
5. runtime routing;
6. client behavior.

До проверки projector и vision route повторять image tests не следует.

#### Clients

Для Qwen3.8 нужны отдельные receipts:

```text
qwen3.8-api.md
qwen3.8-litellm.md
qwen3.8-opencode.md
qwen3.8-pi.md
```

В каждом будет:

- endpoint abstraction;
- public model alias;
- request shape;
- authentication status без раскрытия ключа;
- результат smoke test;
- known limitations.

## QMD

Создана локальная QMD collection:

```text
localllm-kb
```

Она индексирует только:

```text
T:\Code\localllm-kb\kb
```

а не весь `T:\Code` и не весь `servers_team`.

Проверено:

```text
qmd update
qmd search "Qwen3.8 Dynamic V3 artifact rollback" -c localllm-kb --no-rerank
```

Поиск возвращает запись Qwen3.8.

## Проверки

Пройдены:

```text
python -m pytest -q
```

Результат:

```text
3 passed
```

Проверка Markdown-графа:

```text
kb-bootstrap validate --dir kb
```

Результат:

```text
DEAD LINKS: 0
```

QMD успешно обновляет коллекцию `localllm-kb`.

## Что осталось

1. Решить, будет ли локальный checkout позже опубликован как отдельный GitHub repository или останется локальным.
2. Не смешивать это решение с upstream `ozand/kb-bootstrap`.
3. Добавить полноценные Qwen3.8 artifact/runtime/client receipts.
4. Перенести в KB только sanitized результаты из текущего Qwen3.8 исследования.
5. Ссылаться из `servers_team` на записи KB, но не переносить туда всю модельную историю.
6. Сохранить в `servers_team` только операционные сведения:
   - как установлен Unsloth;
   - где находятся launchers;
   - как запускается backend;
   - какие live-service ограничения действуют.
7. Сохранить в `localllm-kb`:
   - почему выбран конкретный artifact;
   - какие были версии и rollback;
   - результаты context/runtime/client validation;
   - известные проблемы Qwen3.8;
   - модельные и runtime-specific ограничения.

