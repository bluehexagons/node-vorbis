declare class Decoder extends require('readable-stream/transform') {
  channels: number
  sampleRate: number
  bitDepth: number
  float: boolean
  signed: boolean

  version: number
  bitrateUpper: number
  bitrateNominal: number
  bitrateLower: number
  bitrateWindow: number
}

export = Decoder
