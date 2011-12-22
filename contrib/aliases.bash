# Este contem facilidades para o shell e é importado pelo postactivate

PROJECT_ROOT="$VIRTUAL_ENV/src"

alias manage="python $PROJECT_ROOT/manage.py"
function autotest () {
    fab autoexec:"python $PROJECT_ROOT/manage.py test -v 0 $*"
}

alias reset_db="manage reset account extrato; manage syncdb; manage loaddata agencies"
alias cdsrc="cd $PROJECT_ROOT"
alias cddjango="cd `virtualenvwrapper_get_site_packages_dir`/django"
alias rmpyc="find . -iname '*.pyc' -exec rm {} \;"
alias fs="git flow feature start"
alias ff="git flow feature finish"

function cover () {

    case $1 in

        html)
            coverage html --omit $VIRTUAL_ENV/lib,/usr -d $VIRTUAL_ENV/coverage
        ;;

        erase)
            coverage erase
            rm -r $VIRTUAL_ENV/coverage
        ;;

        --help)
            echo "cover [ html | erase ]"
            echo "must run cover at least once to use html or erase"
        ;;

        *)
            coverage run $PROJECT_ROOT/manage.py test
            coverage report --omit $VIRTUAL_ENV/lib,/usr -m
        ;;

    esac
}

function _fab_list () {
    # auto completion for fabfiles
    local cur="${COMP_WORDS[COMP_CWORD]}"
    FAB_OPTIONS=$(fab -l | grep '^ ' | awk '{ print $1 }')
    COMPREPLY=( $(compgen -W "$FAB_OPTIONS" -- ${cur}) )

    if [ "${COMPREPLY[*]}" = "$cur" ]
    then
        echo -e "\n$(fab -d $cur)"
        COMPREPLY=""
    fi
}
complete -o default -o nospace -F _fab_list fab

export PYLINTRC="$VIRTUAL_ENV/contrib/pylintrc"
