# Design Document Standard Application Scope

Last Updated: 2026-08-22
Status: CONFIRMED DECISION RECORD

## Purpose

`DESIGN_DOCUMENT_STANDARD.md` を全プロジェクト共通の設計文書統治原則として扱いながら、アプリプロジェクトとは性質が異なる `ai-setup-materials` へ適用する境界を記録する。

## Constitutional Position

`/Users/takashioikawa/Dev/solacom_main/docs/standards/DESIGN_DOCUMENT_STANDARD.md` は、ユーザーが作成する全プロジェクトの設計文書統治における憲法として扱う。

ただし、同標準はアプリプロジェクトを主な適用対象として想定している。教材、Persona、標準資料を管理するRepositoryである `ai-setup-materials` へ、アプリ用の文書構成やテンプレートを100%機械的に適用しない。

## Mandatory Governance Principles

`ai-setup-materials` では、次の統治原則を必須適用する。

- SSOTを明確にする。
- 文書ごとの責務を分離する。
- 命名・表記の一貫性を保つ。
- ヘッダー、状態、版管理を追跡可能にする。
- 文書間の導線を明確にする。
- 履歴を管理し、現行情報と旧情報を区別する。
- AIによる無秩序な文書の追加、変更、統合、削除を禁止する。
- 正本、適用関係、上書き関係を確認できない場合は停止する。
- 重複と更新不整合を防止する。

適用対象外のアプリ用構成があることを理由に、これらの統治原則まで免除してはならない。

## Application-Specific Requirements Not Mechanically Applied

次は、`ai-setup-materials` へ固定要件として機械的に適用しない。

- READMEと6文書を必ず作成する固定構成
- アプリプロジェクト固有の文書名
- UI、データ、API、アーキテクチャ、スクリーンショット等、`ai-setup-materials` に該当しない必須構成

適用対象だけを使用する。固定7文書を `ai-setup-materials` 内へ作成することは、今回の確定事項ではない。

## Notation Normalization Boundary

`English（日本語）` 等の表記統一は、意味、責務、契約、入出力仕様を変えない範囲に限って適用する。

表記変更が確定済みの仕様変更になる箇所は修正せず、例外適用として現行の正式名称・表記を維持する。例外候補には、User確認済みの正式出力名、役割名、判定名、状態名、項目名、列名、固定文言等を含む。ただし、これらを機械的にすべて例外とせず、正本で確定したものに限る。

この例外適用は、現在の確定仕様を表記修正だけで壊さないための一時的な互換性保留であり、永久固定ではない。将来、仕様変更として別途検討し、Userが承認した段階で、`English（日本語）` 表記への統合対象になり得る。

例外は表記の「統一漏れ」と混同せず、例外箇所、根拠、維持理由、再検討条件または解除条件を追跡可能にする。例外を理由に、未期限・無条件で不統一を固定化しない。例外解除をAIが自動決定しない。表記統一を理由にPersonaの機能仕様を再設計しない。

## Unresolved Details

次は未決であり、本記録では推測・決定しない。

- `ai-setup-materials` 向けの具体的な文書体系
- 使用する状態名
- 文書の配置
- 既存文書へ必要な修正
- 7文書を本Repository内へ配置するか、別管理にするか
- 現在の別Repositoryとの不整合をどのように解消するか

## Background Intent

全プロジェクトの設計文書統治に共通する標準の目的を維持しつつ、性質の異なるRepositoryへアプリ用テンプレートを機械適用して、不要な文書や該当しない構成を増やすことを防ぐ。

文書数やアプリ固有の構成を適用しない場合も、SSOT、責務分離、追跡可能性、導線、履歴、変更統制、重複・不整合防止という統治目的は維持する。

文書の一貫性を高めつつ、外見上の統一のために確定済み仕様を壊すことを防ぐ。
