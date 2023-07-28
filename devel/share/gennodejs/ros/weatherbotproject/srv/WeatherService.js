// Auto-generated. Do not edit!

// (in-package weatherbotproject.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class WeatherServiceRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Weather = null;
    }
    else {
      if (initObj.hasOwnProperty('Weather')) {
        this.Weather = initObj.Weather
      }
      else {
        this.Weather = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type WeatherServiceRequest
    // Serialize message field [Weather]
    bufferOffset = _serializer.string(obj.Weather, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WeatherServiceRequest
    let len;
    let data = new WeatherServiceRequest(null);
    // Deserialize message field [Weather]
    data.Weather = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.Weather);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'weatherbotproject/WeatherServiceRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'dea54388e2879333920102ba8c3fe248';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string Weather
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new WeatherServiceRequest(null);
    if (msg.Weather !== undefined) {
      resolved.Weather = msg.Weather;
    }
    else {
      resolved.Weather = ''
    }

    return resolved;
    }
};

class WeatherServiceResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ok = null;
    }
    else {
      if (initObj.hasOwnProperty('ok')) {
        this.ok = initObj.ok
      }
      else {
        this.ok = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type WeatherServiceResponse
    // Serialize message field [ok]
    bufferOffset = _serializer.uint32(obj.ok, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WeatherServiceResponse
    let len;
    let data = new WeatherServiceResponse(null);
    // Deserialize message field [ok]
    data.ok = _deserializer.uint32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'weatherbotproject/WeatherServiceResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'fc98085824fd3dfdd9a20e11d08cfef6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint32 ok
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new WeatherServiceResponse(null);
    if (msg.ok !== undefined) {
      resolved.ok = msg.ok;
    }
    else {
      resolved.ok = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: WeatherServiceRequest,
  Response: WeatherServiceResponse,
  md5sum() { return '456b4033dd09be069e0eb63a859d7454'; },
  datatype() { return 'weatherbotproject/WeatherService'; }
};
