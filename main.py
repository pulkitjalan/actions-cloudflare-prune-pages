import argparse
import CloudFlare

parser = argparse.ArgumentParser(description='Purge Cloudflare Pages cache')
parser.add_argument('--account', required=True, help='Account ID')
parser.add_argument('--project', required=True, help='Pages project name to purge')
parser.add_argument('--keep', type=int, default=3, help='Number of deployments to keep')

args = parser.parse_args()

cf = CloudFlare.CloudFlare()
deployments = cf.accounts.pages.projects.deployments.get(args.account, args.project)
deployments = deployments[args.keep:]

for deployment in deployments:
    print(f'Deleting {deployment["id"]}')
    cf.accounts.pages.projects.deployments.delete(args.account, args.project, deployment["id"])
