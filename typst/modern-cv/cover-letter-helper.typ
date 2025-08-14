// coverletter.typ
// A standalone cover letter template.
// Depends on `helpers.typ` and `lang.toml` in the same directory.

#import "helpers.typ": *

/// ---- Coverletter-Specific Helpers ----

#let __coverletter_footer(
  author,
  language,
  date,
  lang_data,
  use-smallcaps: true,
) = {
  set text(fill: gray, size: 0.73em)
  __justify_align_3[
    #__apply_smallcaps(date, use-smallcaps)
  ][
    #__apply_smallcaps(
      {
        let name = __format_author_name(author, language)
        name + " · " + linguify("cover-letter", from: lang_data)
      },
      use-smallcaps,
    )
  ][
    #context {
      counter(page).display()
    }
  ]
}

#let default-closing(lang_data) = {
  align(bottom)[
    #text(weight: "light", style: "italic")[
      #linguify("attached", from: lang_data)#sym.colon #linguify(
        "curriculum-vitae",
        from: lang_data,
      )]
  ]
}

/// ---- Coverletter Template ----

#let coverletter(
  author: (:),
  profile-picture: image,
  date: datetime.today().display("[month repr:long] [day], [year]"),
  accent-color: default-accent-color,
  language: "en",
  font: ("Source Sans Pro", "Source Sans 3"),
  header-font: "Roboto",
  show-footer: true,
  closing: none,
  paper-size: "a4",
  use-smallcaps: true,
  show-address-icon: false,
  base-font-size: 11pt, 
  body,
) = {
  if type(accent-color) == str {
    accent-color = rgb(accent-color)
  }

  let lang_data = toml("lang.toml")

  if closing == none {
    closing = default-closing(lang_data)
  }

  show: body => context {
    set document(
      author: author.firstname + " " + author.lastname,
      title: linguify("cover-letter", lang: language, from: lang_data),
    )
    body
  }

  set text(
    font: font,
    lang: language,
    size: base-font-size,
    fill: color-darkgray,
    fallback: true,
  )

  set page(
    paper: paper-size,
    margin: (left: 15mm, right: 15mm, top: 10mm, bottom: 10mm),
    footer: if show-footer [#__coverletter_footer(
      author,
      language,
      date,
      lang_data,
      use-smallcaps: use-smallcaps,
    )] else [],
    footer-descent: 2mm,
  )

  set par(spacing: 0.75em, justify: true)
  set heading(numbering: none, outlined: false)

  show heading: it => [
    #set block(above: 1em, below: 1em)
    #set text(size: 1.45em, weight: "regular")
    #align(left)[
      #text[#strong[#text(accent-color)[#it.body]]]
      #box(width: 1fr, line(length: 100%))
    ]
  ]

  let name = {
    align(right)[
      #pad(bottom: 5pt)[
        #block[
          #set text(size: 2.9em, style: "normal", font: header-font)
          #if language == "zh" or language == "ja" [
            #text(accent-color, weight: "thin")[#author.firstname]#text(weight: "bold")[#author.lastname]
          ] else [
            #text(accent-color, weight: "thin")[#author.firstname]
            #text(weight: "bold")[#author.lastname]
          ]
        ]
      ]
    ]
  }

  let positions = {
    set text(accent-color, size:  0.82em, weight: "regular")
    align(right)[
      #__apply_smallcaps(
        author.positions.join(text[#"  "#sym.dot.c#"  "]),
        use-smallcaps,
      )
    ]
  }

  let address = {
    set text(size:  0.82em, weight: "bold", fill: color-gray)
    align(right)[
      #if ("address" in author) [
        #if show-address-icon [
          #address-icon
          #box[#text(author.address)]
        ] else [
          #text(author.address)
        ]
      ]
    ]
  }

  let contacts = {
    set box(height: 9pt)
    let separator = [ #box(sym.bar.v) ]
    let author_list = ()

    if ("phone" in author) {
      author_list.push[
        #phone-icon
        #box[#link("tel:" + author.phone)[#author.phone]]
      ]
    }
    if ("email" in author) {
      author_list.push[
        #email-icon
        #box[#link("mailto:" + author.email)[#author.email]]
      ]
    }
    if ("github" in author) {
      author_list.push[
        #github-icon
        #box[#link("https://github.com/" + author.github)[#author.github]]
      ]
    }
    if ("linkedin" in author) {
      author_list.push[
        #linkedin-icon
        #box[
          #link("https://www.linkedin.com/in/" + author.linkedin)[#author.firstname #author.lastname]
        ]
      ]
    }
    if ("orcid" in author) {
      author_list.push[
        #orcid-icon
        #box[#link("https://orcid.org/" + author.orcid)[#author.orcid]]
      ]
    }
    if ("website" in author) {
      author_list.push[
        #website-icon
        #box[#link(author.website)[#author.website]]
      ]
    }

    if ("custom" in author and type(author.custom) == array) {
      for item in author.custom {
        if ("text" in item) {
          author_list.push[
            #if ("icon" in item) [
              #box(fa-icon(item.icon, fill: color-darknight))
            ]
            #box[
              #if ("link" in item) [
                #link(item.link)[#item.text]
              ] else [
                #item.text
              ]
            ]
          ]
        }
      }
    }

    align(right)[
      #set text(size: 0.73em, weight: "light", style: "normal")
      #author_list.join(separator)
    ]
  }

  let letter-heading = {
    grid(
      columns: (1fr, 2fr),
      rows: 100pt,
      align(left + horizon)[
        #block(
          clip: true,
          stroke: 0pt,
          radius: 2cm,
          width: 4cm,
          height: auto,
          profile-picture,
        )
      ],
      [
        #name
        #positions
        #address
        #contacts
      ],
    )
  }

  let signature = {
    align(bottom)[
      #pad(bottom: 2em)[
        #text(weight: "light")[#linguify("sincerely", from: lang_data)#if (
          language != "de"
        ) [#sym.comma]] \
        #text(weight: "bold")[#author.firstname #author.lastname] \ \
      ]
    ]
  }

  letter-heading
  body
  linebreak()
  signature
  closing
}

#let hiring-entity-info(
  entity-info: (:),
  date: datetime.today().display("[month repr:long] [day], [year]"),
  use-smallcaps: true,
) = {
  set par(leading: 1em)
  pad(top: 1.5em, bottom: 1.5em)[
    #__justify_align[
      #text(weight: "bold", size: 1.1em)[#entity-info.target]
    ][
      #text(weight: "light", style: "italic", size:0.82em)[#date]
    ]

    #pad(top: 0.65em, bottom: 0.65em)[
      #text(weight: "regular", fill: color-gray, size: 0.82em)[
        #__apply_smallcaps(entity-info.name, use-smallcaps) \
        #entity-info.street-address \
        #entity-info.city \
      ]
    ]
  ]
}

#let letter-heading(job-position: "", addressee: "", dear: "") = {
  let lang_data = toml("lang.toml")
  underline(evade: false, stroke: 0.5pt, offset: 0.3em)[
    #text(weight: "bold", size: 1.1em)[#linguify(
      "letter-position-pretext",
      from: lang_data,
    ) #job-position]
  ]
  pad(top: 1em, bottom: 1em)[
    #text(weight: "light", fill: color-gray)[
      #if dear == "" [
        #linguify("dear", from: lang_data)
      ] else [
        #dear
      ]
      #addressee,
    ]
  ]
}

#let coverletter-content(content) = {
  pad(top: 1em, bottom: 1em)[
    #set par(first-line-indent: 3em)
    #set text(weight: "light")
    #content
  ]
}