#TODO
#!/usr/bin/env bash	

SOURCEDIR="$1"
REPOSDIR="$2"
REPOSPATH="${SOURCEDIR}/${REPOSDIR}"
    
REPOS=$() \
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