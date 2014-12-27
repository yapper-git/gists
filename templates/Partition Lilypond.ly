\version "2.18.2"
\include "italiano.ly"

\header{
    title = "Titre du morceau"
    subtitle = "Sous-titre"
    poet = ""
    composer = "Compositeur"
    meter = "Style"
    opus = ""
    arranger = ""
    instrument = ""
    dedication = ""
    piece = ""
    head = ""
    copyright = ""
    footer = ""
    tagline = ""
}

global = {
    \key sol \major
    \time 4/4
    %\dynamicUp
    \tempo 4 = 100
}

soprano = \relative do' {
    \clef treble
    %\autoBeamOff

    \voiceOne
    do1 |%mesure 1
    re2 re |
    mi4 mi mi r |%mesure 3
    fad8. sol16 fa4( fa) fa
    \bar "||"
    \oneVoice
}

alto = \relative do' {
    \clef treble

    \voiceTwo
    do1 |%mesure 1
    do2 do |
    do4 do do r |%mesure 3
    do8. do16 do4( do) do
    \bar "||"
    \oneVoice
}

tenor = \relative do {
    \clef bass

    \voiceThree
    fad1 |%1
    fad4 fad fad fad |
    fa fa fa fa |
    fad fad fad fad
    \bar "||"
    \oneVoice
}

bass = \relative do {
    \clef bass

    \voiceFour
    \oneVoice
}

stropheUn = \lyricmode {
    \set stanza = "1. "

    Bla -- bla bli
}

\score { <<
    \new ChoirStaff <<
        % Portée du haut: soprane + alto + paroles attachées à la soprane
        \new Staff <<
            \new Voice = "soprano" << \global \soprano >>
            \new Voice = "alto" << \global \alto >>
            \lyricsto "soprano" \new Lyrics \stropheUn
        >>
        % Portée du bas: ténor + basse
        \new Staff <<
            \new Voice = "tenor" << \global \tenor >>
            \new Voice = "bass" << \global \bass >>
        >>
    >>
>> }
