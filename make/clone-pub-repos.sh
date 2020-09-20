#!/usr/bin/env bash	
#Clones all public repos in a github account to be used within documention.

SOURCEDIR="$1"
REPOSDIR="$2"
REPOSPATH="${SOURCEDIR}/${REPOSDIR}"
GHUSER="cloudoutloud"
    
REPOS=$(curl -s https://api.github.com/users/$GHUSER/repos | jq '.[]|.html_url') \
&& rm -fr $REPOSPATH \
&& mkdir -p $REPOSPATH \
&& cd $REPOSPATH && echo "Changed directory" || exit 1

for REPO in $REPOS; do
    if [[ "$REPO" =~ "zzz_" ]]; then
        echo "Skipped: $REPO"
    else
        echo "Cloning: $REPO"
        git clone --depth 1 $REPO --branch master --single-branch \
        && echo "Repo cloned successfully" \
        || echo "Issue cloning repo"
    fi
done

cd -