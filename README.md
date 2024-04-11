# CloudFlare Prune Pages

This action will prune old CloudFlare Pages deployment. By default it will delete the `preview` deployments, but optionally can be changed to `production` deployments.

## Inputs

Be sure to use a secure method such as [Encrypted Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) for storing/accessing CloudFlare API Key:

| Name | Required | Description | Default |
| --- | --- | --- | --- |
| apiToken | Yes | Your CloudFlare api token. | |
| accountId | Yes | Your CloudFlare account id. | |
| projectName | Yes | Your CloudFlare project name. | |
| environment | No | Environment to prune, `production` or `preview`. | preview |
| keep | No | Number of deployments to keep. | 3 |

## Usage

Example:

```yml
on: [push]

permissions:
    contents: read
    deployments: write

jobs:
  publish:
    runs-on: ubuntu-latest
    name: Publish to CloudFlare Pages
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      # Run a build step here if your project requires

      - name: Publish to CloudFlare Pages
        uses: cloudflare/pages-action@v1
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: YOUR_ACCOUNT_ID
          projectName: YOUR_PROJECT_NAME
          directory: YOUR_BUILD_OUTPUT_DIRECTORY
          # Optional: Enable this if you want to have GitHub Deployments triggered
          gitHubToken: ${{ secrets.GITHUB_TOKEN }}
          # Optional: Switch what branch you are publishing to.
          # By default this will be the branch which triggered this workflow
          branch: main
          # Optional: Change the working directory
          workingDirectory: my-site
          # Optional: Change the Wrangler version, allows you to point to a specific version or a tag such as `beta`
          wranglerVersion: '3'

      - name: Prune old CloudFlare Pages deployments
        uses: pulkitjalan/actions-cloudflare-prune-pages@v1
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: YOUR_ACCOUNT_ID
          projectName: YOUR_PROJECT_NAME
          # Optional: Switch the environment to production (Default: preview)
          environment: production
          # Optional: Change the number of deployments to keep (Default: 3)
          keep: 5
```