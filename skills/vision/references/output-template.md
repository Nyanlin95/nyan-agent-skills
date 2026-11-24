# Output template (from-scratch mode)

On the board and in VISION.md:

    # Vision

    `{project}` exists so that {the one-sentence reason the project exists}.
    It serves {the named user}, and it {what it turns their input into}.
    It owns exactly one thing: {the single owned surface}.

    ## {Principle section, 3-6 of these}

    {Declarative, testable, present-tense lines; one sentence per line.}
    {Explicit boundaries: what is welcome, what is refused, and why.}

    ## Scope

    {What this project is not, named concretely.}
    {Where personal/private material stays, if applicable.}
    {How the repo holds itself to its own standard, if applicable.}

    A change aligns when {testable positive criteria}.
    A change should be resisted when {testable negative criteria}.

In STRATEGY.md, the same text one heading level lower, with the approval
marker (a new file gets only the title line above it):

    # {project} Strategy

    ## Vision

    <!-- vision: author-approved YYYY-MM-DD -->

    `{project}` exists so that ...

    ### {Principle section, 3-6 of these}

    ...

    ### Scope

    ...

    ## {Other writers' sections, unchanged}
