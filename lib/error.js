
/**
 * Module dependencies.
 */

var inherits = require('util').inherits;
var binding = require('./binding');

/**
 * Module exports.
 */

module.exports = VorbisError;

/**
 * Map of error names and error messages.
 */

var messages = {
  OV_FALSE: 'Not true, or no data available',
  OV_EOF: 'Reached end of file.',
  OV_HOLE: 'Vorbisfile encoutered missing or corrupt data in the bitstream. Recovery is normally automatic and this return code is for informational purposes only.',
  OV_EREAD: 'Read error while fetching compressed data for decode',
  OV_EFAULT: 'Internal inconsistency in encode or decode state. Continuing is likely not possible.',
  OV_EIMPL: 'Feature not implemented',
  OV_EINVAL: 'Either an invalid argument, or incompletely initialized argument passed to a call',
  OV_ENOTVORBIS: 'The given file/data was not recognized as Ogg Vorbis data.',
  OV_EBADHEADER: 'The file/data is apparently an Ogg Vorbis stream, but contains a corrupted or undecipherable header.',
  OV_EVERSION: 'The bitstream format revision of the given stream is not supported.',
  OV_ENOTAUDIO: 'The packet is not an audio packet.',
  OV_EBADPACKET: 'There was an error in the packet.',
  OV_EBADLINK: 'The given link exists in the Vorbis data stream, but is not decipherable due to garbacge or corruption.',
  OV_ENOSEEK: 'The given stream is not seekable'
};

/**
 * Error codes.
 */
var codes = {};
var errors = {};
for (var errorName in messages) {
  var code = binding[errorName];
  errors[errorName] = code;
  codes[code] = errorName;
}

/**
 * The `VorbisError` class.
 */

function VorbisError (code, func) {
  var name = codes[code];
  var message = name + ': ' + messages[name];
  if (func) {
    message = func + '() failed: ' + message;
  }
  Error.call(this);
  Error.captureStackTrace(this, VorbisError);
  this.code = code;
  this.name = name;
  this.message = message;
}
inherits(VorbisError, Error);
