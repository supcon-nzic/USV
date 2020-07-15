// Auto-generated. Do not edit!

// (in-package sailing_robot.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let sensor_msgs = _finder('sensor_msgs');

//-----------------------------------------------------------

class gpswtime {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.fix = null;
      this.time_h = null;
      this.time_m = null;
      this.time_s = null;
    }
    else {
      if (initObj.hasOwnProperty('fix')) {
        this.fix = initObj.fix
      }
      else {
        this.fix = new sensor_msgs.msg.NavSatFix();
      }
      if (initObj.hasOwnProperty('time_h')) {
        this.time_h = initObj.time_h
      }
      else {
        this.time_h = 0;
      }
      if (initObj.hasOwnProperty('time_m')) {
        this.time_m = initObj.time_m
      }
      else {
        this.time_m = 0;
      }
      if (initObj.hasOwnProperty('time_s')) {
        this.time_s = initObj.time_s
      }
      else {
        this.time_s = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type gpswtime
    // Serialize message field [fix]
    bufferOffset = sensor_msgs.msg.NavSatFix.serialize(obj.fix, buffer, bufferOffset);
    // Serialize message field [time_h]
    bufferOffset = _serializer.uint16(obj.time_h, buffer, bufferOffset);
    // Serialize message field [time_m]
    bufferOffset = _serializer.uint16(obj.time_m, buffer, bufferOffset);
    // Serialize message field [time_s]
    bufferOffset = _serializer.uint16(obj.time_s, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type gpswtime
    let len;
    let data = new gpswtime(null);
    // Deserialize message field [fix]
    data.fix = sensor_msgs.msg.NavSatFix.deserialize(buffer, bufferOffset);
    // Deserialize message field [time_h]
    data.time_h = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [time_m]
    data.time_m = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [time_s]
    data.time_s = _deserializer.uint16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += sensor_msgs.msg.NavSatFix.getMessageSize(object.fix);
    return length + 6;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sailing_robot/gpswtime';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '40d5a21afc2b40bb67f25cf656a9b364';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Message for GPS fix with time
    sensor_msgs/NavSatFix fix
    uint16 time_h
    uint16 time_m
    uint16 time_s
    
    ================================================================================
    MSG: sensor_msgs/NavSatFix
    # Navigation Satellite fix for any Global Navigation Satellite System
    #
    # Specified using the WGS 84 reference ellipsoid
    
    # header.stamp specifies the ROS time for this measurement (the
    #        corresponding satellite time may be reported using the
    #        sensor_msgs/TimeReference message).
    #
    # header.frame_id is the frame of reference reported by the satellite
    #        receiver, usually the location of the antenna.  This is a
    #        Euclidean frame relative to the vehicle, not a reference
    #        ellipsoid.
    Header header
    
    # satellite fix status information
    NavSatStatus status
    
    # Latitude [degrees]. Positive is north of equator; negative is south.
    float64 latitude
    
    # Longitude [degrees]. Positive is east of prime meridian; negative is west.
    float64 longitude
    
    # Altitude [m]. Positive is above the WGS 84 ellipsoid
    # (quiet NaN if no altitude is available).
    float64 altitude
    
    # Position covariance [m^2] defined relative to a tangential plane
    # through the reported position. The components are East, North, and
    # Up (ENU), in row-major order.
    #
    # Beware: this coordinate system exhibits singularities at the poles.
    
    float64[9] position_covariance
    
    # If the covariance of the fix is known, fill it in completely. If the
    # GPS receiver provides the variance of each measurement, put them
    # along the diagonal. If only Dilution of Precision is available,
    # estimate an approximate covariance from that.
    
    uint8 COVARIANCE_TYPE_UNKNOWN = 0
    uint8 COVARIANCE_TYPE_APPROXIMATED = 1
    uint8 COVARIANCE_TYPE_DIAGONAL_KNOWN = 2
    uint8 COVARIANCE_TYPE_KNOWN = 3
    
    uint8 position_covariance_type
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    # 0: no frame
    # 1: global frame
    string frame_id
    
    ================================================================================
    MSG: sensor_msgs/NavSatStatus
    # Navigation Satellite fix status for any Global Navigation Satellite System
    
    # Whether to output an augmented fix is determined by both the fix
    # type and the last time differential corrections were received.  A
    # fix is valid when status >= STATUS_FIX.
    
    int8 STATUS_NO_FIX =  -1        # unable to fix position
    int8 STATUS_FIX =      0        # unaugmented fix
    int8 STATUS_SBAS_FIX = 1        # with satellite-based augmentation
    int8 STATUS_GBAS_FIX = 2        # with ground-based augmentation
    
    int8 status
    
    # Bits defining which Global Navigation Satellite System signals were
    # used by the receiver.
    
    uint16 SERVICE_GPS =     1
    uint16 SERVICE_GLONASS = 2
    uint16 SERVICE_COMPASS = 4      # includes BeiDou.
    uint16 SERVICE_GALILEO = 8
    
    uint16 service
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new gpswtime(null);
    if (msg.fix !== undefined) {
      resolved.fix = sensor_msgs.msg.NavSatFix.Resolve(msg.fix)
    }
    else {
      resolved.fix = new sensor_msgs.msg.NavSatFix()
    }

    if (msg.time_h !== undefined) {
      resolved.time_h = msg.time_h;
    }
    else {
      resolved.time_h = 0
    }

    if (msg.time_m !== undefined) {
      resolved.time_m = msg.time_m;
    }
    else {
      resolved.time_m = 0
    }

    if (msg.time_s !== undefined) {
      resolved.time_s = msg.time_s;
    }
    else {
      resolved.time_s = 0
    }

    return resolved;
    }
};

module.exports = gpswtime;
