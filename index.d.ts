import VorbisDecoder from './lib/decoder'
import VorbisEncoder from './lib/encoder'

declare module Vorbis {
  export function isVorbis(oggPacket: any, callback: (result: boolean) => void): void
  export const Decoder = VorbisDecoder
  export const Encoder = VorbisEncoder
  export const version: number
}

export = Vorbis
