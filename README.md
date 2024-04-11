# CloudFlare Prune Pages

This action will prune old CloudFlare Pages deployment. By default it will delete the `preview` deployments, but optionally can be changed to `production` deployments.

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
    name: Publish to Cloudflare Pages
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      # Run a build step here if your project requires

      - name: Publish to Cloudflare Pages
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

      - name: Prune old Cloudflare Pages deployments
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