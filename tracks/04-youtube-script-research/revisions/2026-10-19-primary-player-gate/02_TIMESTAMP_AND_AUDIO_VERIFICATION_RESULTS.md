# 02 — Timestamp and Audio Verification Results
**Method:** Attempt to access each ORIGINAL YouTube watch page and its ordinary **Show transcript** UI, then listen within the native player at genuine cue onsets if accessible. Only old narration-order descriptions were carried forward. These are not timestamp candidates.
**Status definitions:** `TIMESTAMPS_NOT_VERIFIED` = no observed original cue mm:ss; `AUDIO_NOT_CHECKED` = original audible media could not be sampled; `UNDETERMINED_PLAYER_INACCESSIBLE` = cannot tell whether the feature is available or absent for that video.
**No timestamps were estimated** from length, character position, word count, or source-story clock time.

## V01 — Seine 'WAHNSINNIGE' Entscheidung Im Minenfeld — Warum US-Soldaten Ihm Ein Denkmal Errichteten

- Original watch URL: https://www.youtube.com/watch?v=m4jgcD-m1tA
- Prior subtitle class: unsegmented text, no independently verified native cues.
- Show transcript status: `UNDETERMINED_PLAYER_INACCESSIBLE`.
- Original video audio status: `AUDIO_NOT_CHECKED`.
- Relevant blocker: `WEB_DIRECT_FETCH_DISABLED`; Direct official watch-page fetch returned DisabledError; connected browser exposes no YouTube tab; container HTTP request cannot resolve YouTube domain.

| Anchor | Native playback mm:ss | Prior narration-order observation (NOT a timecode) | Original audio |
|---|---|---|---|
| opening | **NOT_VERIFIED** | Dated minefield rescue dilemma; uttered 10:37 is the story clock, not playback mm:ss | **NOT_CHECKED** |
| first_payoff | **NOT_VERIFIED** | Wounded American and request for help; moral dilemma established | **NOT_CHECKED** |
| middle_transition | **NOT_VERIFIED** | Minefield waiting -> rescue party enters | **NOT_CHECKED** |
| ending | **NOT_VERIFIED** | Fatal attempt and veterans memorial reframed as moral choice | **NOT_CHECKED** |

**Inference ceiling:** narrative order from prior captions only; exact first-payoff latency, mid-video transition time, silence, pitch, emotional delivery, and speaker identity are not verifiable in this attempt.


## V04 — Why the B-58 Hustler Became Obsolete So Quickly

- Original watch URL: https://www.youtube.com/watch?v=6MiVIhzzepo
- Prior subtitle class: unsegmented text, no independently verified native cues.
- Show transcript status: `UNDETERMINED_PLAYER_INACCESSIBLE`.
- Original video audio status: `AUDIO_NOT_CHECKED`.
- Relevant blocker: `WEB_FETCH_THROTTLED`; Direct official watch-page fetch returned Online fetch throttled; connected browser exposes no YouTube tab; container HTTP request cannot resolve YouTube domain.

| Anchor | Native playback mm:ss | Prior narration-order observation (NOT a timecode) | Original audio |
|---|---|---|---|
| opening | **NOT_VERIFIED** | B-58 speed/mission framed against packaging constraint | **NOT_CHECKED** |
| first_payoff | **NOT_VERIFIED** | High-speed bomber design explains narrow airframe and subsystem compromises | **NOT_CHECKED** |
| middle_transition | **NOT_VERIFIED** | Component tour -> operational testing/crew protection | **NOT_CHECKED** |
| ending | **NOT_VERIFIED** | Soviet defenses and ICBMs undercut role; U-2 next-video bridge | **NOT_CHECKED** |

**Inference ceiling:** narrative order from prior captions only; exact first-payoff latency, mid-video transition time, silence, pitch, emotional delivery, and speaker identity are not verifiable in this attempt.


## V07 — We're Going From Summer STRAIGHT To Winter...

- Original watch URL: https://www.youtube.com/watch?v=V_jpV8ijQ_Y
- Prior subtitle class: unsegmented text, no independently verified native cues.
- Show transcript status: `UNDETERMINED_PLAYER_INACCESSIBLE`.
- Original video audio status: `AUDIO_NOT_CHECKED`.
- Relevant blocker: `WEB_FETCH_THROTTLED`; Direct official watch-page fetch returned Online fetch throttled; connected browser exposes no YouTube tab; container HTTP request cannot resolve YouTube domain.

| Anchor | Native playback mm:ss | Prior narration-order observation (NOT a timecode) | Original audio |
|---|---|---|---|
| opening | **NOT_VERIFIED** | Heat-to-freeze forecast warning | **NOT_CHECKED** |
| first_payoff | **NOT_VERIFIED** | Early St Louis numerical temperature swing | **NOT_CHECKED** |
| middle_transition | **NOT_VERIFIED** | Storm retrospective -> sponsor -> forecast mechanics | **NOT_CHECKED** |
| ending | **NOT_VERIFIED** | Model uncertainty and next-week warm rebound | **NOT_CHECKED** |

**Inference ceiling:** narrative order from prior captions only; exact first-payoff latency, mid-video transition time, silence, pitch, emotional delivery, and speaker identity are not verifiable in this attempt.


## Cross-case interpretation

All three remain caption-only. The absence of observed native timestamps is an **access failure**, not a claim of unavailable captions. A prior transcript, metadata, thumbnail, or third-party source must not be relabeled as an on-player timestamp. V10 is explicitly out of scope and retains its prior mirrored-timing, audio-unverified label.
