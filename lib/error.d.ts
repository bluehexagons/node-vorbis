export = class VorbisError extends Error {
  message: string
  stack: string
  code: number
  constructor(code: number, funcName: string)
}