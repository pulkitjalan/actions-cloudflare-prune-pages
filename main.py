import argparse
import CloudFlare

parser = argparse.ArgumentParser(description='Purge Cloudflare Pages cache')
parser.add_argument('--accountId', required=True, help='Account ID')
parser.add_argument('--projectName', required=True, help='Pages project name to purge')
parser.add_argument('--environment', default='preview', choices=['production', 'preview'], help='The environment to purge')
parser.add_argument('--keep', type=int, default=3, help='Number of deployments to keep')

args = parser.parse_args()

cf = CloudFlare.CloudFlare()
deployments = cf.accounts.pages.projects.deployments.get(args.accountId, args.projectName, params = {'env': args.environment})

deployments = deployments[args.keep:]

for deployment in deployments:
    print(f'Deleting {deployment["id"]}')
    cf.accounts.pages.projects.deployments.delete(args.accountId, args.projectName, deployment["id"])
