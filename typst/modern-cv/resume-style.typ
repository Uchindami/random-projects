// resume.typ
// A standalone resume template.
// Depends on `helpers.typ` and `lang.toml` in the same directory.

#import "helpers.typ": *

/// ---- Resume-Specific Helpers ----

#let __resume_footer(author, language, lang_data, date, use-smallcaps: true) = {
  set text(fill: gray, size: 8pt)
  __justify_align_3[
    #__apply_smallcaps(date, use-smallcaps)
  ][
    #__apply_smallcaps(
      {
        let name = __format_author_name(author, language)
        name + " · " + linguify("resume", from: lang_data)
      },
      use-smallcaps,
    )
  ][
    #context {
      counter(page).display()
    }
  ]
}

#let github-link(github-path) = {
  set box(height: 11pt)
  align(right + horizon)[
    #fa-icon("github", fill: color-darkgray) #link(
      "https://github.com/" + github-path,
      github-path,
    )
  ]
}

#let secondary-right-header(body) = {
  set text(size: 11pt, weight: "medium")
  body
}

#let tertiary-right-header(body) = {
  set text(weight: "light", size: 9pt)
  body
}

#let justified-header(primary, secondary) = {
  set block(above: 0.7em, below: 0.7em)
  pad[
    #__justify_align[
      == #primary
    ][
      #secondary-right-header[#secondary]
    ]
  ]
}

#let secondary-justified-header(primary, secondary) = {
  __justify_align[
    === #primary
  ][
    #tertiary-right-header[#secondary]
  ]
}

/// ---- Resume Template ----

#let resume(
  author: (:),
  profile-picture: image,
  date: datetime.today().display("[month repr:long] [day], [year]"),
  accent-color: default-accent-color,
  colored-headers: true,
  show-footer: true,
  language: "en",
  font: ("Source Sans Pro", "Source Sans 3"),
  header-font: "Roboto",
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

  show: body => context {
    set document(
      author: author.firstname + " " + author.lastname,
      title: linguify("resume", lang: language, from: lang_data),
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
    footer: if show-footer [#__resume_footer(
      author,
      language,
      lang_data,
      date,
      use-smallcaps: use-smallcaps,
    )] else [],
    footer-descent: 0pt,
  )

  set par(spacing: 0.75em, justify: true)
  set heading(numbering: none, outlined: false)

  show heading.where(level: 1): it => [
    #set text(size:  1.45em, weight: "regular")
    #set align(left)
    #set block(above: 1em)
    #let color = if colored-headers {
      accent-color
    } else {
      color-darkgray
    }
    #text[#strong[#text(color)[#it.body]]]
    #box(width: 1fr, line(length: 100%))
  ]

  show heading.where(level: 2): it => {
    set text(color-darkgray, size: 1.1em, style: "normal", weight: "bold")
    it.body
  }

  show heading.where(level: 3): it => {
    set text(size: 0.9em, weight: "regular")
    __apply_smallcaps(it.body, use-smallcaps)
  }

  let name = {
    align(center)[
      #pad(bottom: 5pt)[
        #block[
          #set text(size:  2.9em, style: "normal", font: header-font)
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
    set text(accent-color, size: 0.82em, weight: "regular")
    align(center)[
      #__apply_smallcaps(
        author.positions.join(text[#"  "#sym.dot.c#"  "]),
        use-smallcaps,
      )
    ]
  }

  let address = {
    set text(size: 0.82em, weight: "regular")
    align(center)[
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
    set box(height: 0.82em)
    let separator = box(width: 5pt)
    align(center)[
      #set text(size: 0.82em, weight: "regular", style: "normal")
      #block[
        #align(horizon)[
          #if ("birth" in author) [
            #birth-icon
            #box[#text(author.birth)]
            #separator
          ]
          #if ("phone" in author) [
            #phone-icon
            #box[#link("tel:" + author.phone)[#author.phone]]
            #separator
          ]
          #if ("email" in author) [
            #email-icon
            #box[#link("mailto:" + author.email)[#author.email]]
          ]
          #if ("homepage" in author) [
            #separator
            #homepage-icon
            #box[#link(author.homepage)[#author.homepage]]
          ]
          #if ("github" in author) [
            #separator
            #github-icon
            #box[#link("https://github.com/" + author.github)[#author.github]]
          ]
          #if ("gitlab" in author) [
            #separator
            #gitlab-icon
            #box[#link("https://gitlab.com/" + author.gitlab)[#author.gitlab]]
          ]
          #if ("bitbucket" in author) [
            #separator
            #bitbucket-icon
            #box[#link("https://bitbucket.org/" + author.bitbucket)[#author.bitbucket]]
          ]
          #if ("linkedin" in author) [
            #separator
            #linkedin-icon
            #box[
              #link("https://www.linkedin.com/in/" + author.linkedin)[#author.firstname #author.lastname]
            ]
          ]
          #if ("twitter" in author) [
            #separator
            #twitter-icon
            #box[#link("https://twitter.com/" + author.twitter)[\@#author.twitter]]
          ]
          #if ("scholar" in author) [
            #let fullname = str(author.firstname + " " + author.lastname)
            #separator
            #google-scholar-icon
            #box[#link("https://scholar.google.com/citations?user=" + author.scholar)[#fullname]]
          ]
          #if ("orcid" in author) [
            #separator
            #orcid-icon
            #box[#link("https://orcid.org/" + author.orcid)[#author.orcid]]
          ]
          #if ("website" in author) [
            #separator
            #website-icon
            #box[#link(author.website)[#author.website]]
          ]
          #if ("custom" in author and type(author.custom) == array) [
            #for item in author.custom [
              #if ("text" in item) [
                #separator
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
            ]
          ]
        ]
      ]
    ]
  }

  if profile-picture != none {
    grid(
      columns: (100% - 4cm, 4cm),
      rows: 100pt,
      gutter: 10pt,
      [
        #name
        #positions
        #address
        #contacts
      ],
      align(left + horizon)[
        #block(
          clip: true,
          stroke: 0pt,
          radius: 2cm,
          width: 4cm,
          height: 4cm,
          profile-picture,
        )
      ],
    )
  } else {
    name
    positions
    address
    contacts
  }

  body
}

#let resume-item(body) = {
  set text(size: 10pt, style: "normal", weight: "light", fill: color-darknight)
  set block(above: 0.75em, below: 1.25em)
  set par(leading: 0.65em)
  block(above: 0.5em)[
    #body
  ]
}

#let resume-entry(
  title: none,
  location: "",
  date: "",
  description: "",
  title-link: none,
  accent-color: default-accent-color,
  location-color: default-location-color,
) = {
  let title-content
  if type(title-link) == str {
    title-content = link(title-link)[#title]
  } else {
    title-content = title
  }
  block(above: 1em, below: 0.65em)[
    #pad[
      #justified-header(title-content, location)
      #if description != "" or date != "" [
        #secondary-justified-header(description, date)
      ]
    ]
  ]
}

#let resume-gpa(numerator, denominator) = {
  set text(size: 12pt, style: "italic", weight: "light")
  text[Cumulative GPA: #box[#strong[#numerator] / #denominator]]
}

#let resume-certification(certification, date) = {
  justified-header(certification, date)
}

#let resume-skill-category(category) = {
  align(left)[
    #set text(hyphenate: false)
    == #category
  ]
}

#let resume-skill-values(values) = {
  align(left)[
    #set text(size: 11pt, style: "normal", weight: "light")
    #values.join(", ")
  ]
}

#let resume-skill-item(category, items) = {
  set block(below: 0.65em)
  set pad(top: 2pt)
  pad[
    #grid(
      columns: (3fr, 8fr),
      gutter: 10pt,
      resume-skill-category(category), resume-skill-values(items),
    )
  ]
}

#let resume-skill-grid(categories_with_values: (:)) = {
  set block(below: 1.25em)
  set pad(top: 2pt)
  pad[
    #grid(
      columns: (auto, auto),
      gutter: 10pt,
      ..categories_with_values
        .pairs()
        .map(((key, value)) => (
          resume-skill-category(key),
          resume-skill-values(value),
        ))
        .flatten()
    )
  ]
}