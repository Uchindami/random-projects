// helpers.typ
// Contains shared constants and helper functions for the resume and cover letter templates.

#import "@preview/fontawesome:0.5.0": *
#import "@preview/linguify:0.4.2": *

// const color
#let color-darknight = rgb("#131A28")
#let color-darkgray = rgb("#333333")
#let color-gray = rgb("#5d5d5d")
#let default-accent-color = rgb("#262F99")
#let default-location-color = rgb("#333333")

// const icons
#let linkedin-icon = box(fa-icon("linkedin", fill: color-darknight))
#let github-icon = box(fa-icon("github", fill: color-darknight))
#let gitlab-icon = box(fa-icon("gitlab", fill: color-darknight))
#let bitbucket-icon = box(fa-icon("bitbucket", fill: color-darknight))
#let twitter-icon = box(fa-icon("twitter", fill: color-darknight))
#let google-scholar-icon = box(fa-icon("google-scholar", fill: color-darknight))
#let orcid-icon = box(fa-icon("orcid", fill: color-darknight))
#let phone-icon = box(fa-icon("square-phone", fill: color-darknight))
#let email-icon = box(fa-icon("envelope", fill: color-darknight))
#let birth-icon = box(fa-icon("cake", fill: color-darknight))
#let homepage-icon = box(fa-icon("home", fill: color-darknight))
#let website-icon = box(fa-icon("globe", fill: color-darknight))
#let address-icon = box(fa-icon("location-crosshairs", fill: color-darknight))

/// Helpers

// Common helper functions
#let __format_author_name(author, language) = {
  if language == "zh" or language == "ja" {
    str(author.firstname) + str(author.lastname)
  } else {
    str(author.firstname) + " " + str(author.lastname)
  }
}

#let __apply_smallcaps(content, use-smallcaps) = {
  if use-smallcaps {
    smallcaps(content)
  } else {
    content
  }
}

// layout utility
#let __justify_align(left_body, right_body) = {
  block[
    #left_body
    #box(width: 1fr)[
      #align(right)[
        #right_body
      ]
    ]
  ]
}

#let __justify_align_3(left_body, mid_body, right_body) = {
  block[
    #box(width: 1fr)[
      #align(left)[
        #left_body
      ]
    ]
    #box(width: 1fr)[
      #align(center)[
        #mid_body
      ]
    ]
    #box(width: 1fr)[
      #align(right)[
        #right_body
      ]
    ]
  ]
}